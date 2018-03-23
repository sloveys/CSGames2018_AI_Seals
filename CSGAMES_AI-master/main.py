import argparse
import importlib
from ast import literal_eval

import time
from flask import Flask
from flask_socketio import SocketIO, emit
from py4j.java_gateway import JavaGateway
from src.command.CommandFactory import CommandFactory
from src.game.Game import Game
import threading
import os
from queue import Queue

if __name__ == '__main__':
    app = Flask(__name__)
    socketio = SocketIO(app)

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', help='Map name')
    parser.add_argument('-p', help='Python bots names', nargs='+')
    parser.add_argument('-j', help='Use java', dest='j', action='store_true')
    parser.set_defaults(j=False)

    args = parser.parse_args()

    bots = []
    for bot in args.p:
        name = 'src.bot.' + bot
        mod = importlib.import_module(name)
        bot = getattr(mod, bot)
        bots.append(bot())

    if args.j:
        gateway = JavaGateway(auto_convert=True)
        java_bots = gateway.entry_point.getBots()
        for bot in java_bots:
            bots.append(java_bots[0])

    game = Game(len(bots), os.path.join(os.getcwd(), 'maps', args.m))

    def get_other_players(player_turn, players):
        other_player = []
        for player in players:
            if player['id'] != player_turn:
                other_player.append(player)
        return other_player

    def run_bot_turn(q, ai, game, character, players):
        try:
            q.put(ai.turn(game, character, players))
        except Exception as e:
            print(e)
            time.sleep(1)

    def parse_player_info(info):
        bot_state = literal_eval(info['player_info'])
        for i, bot in enumerate(bot_state):
            bot = literal_eval(bot)
            for key in bot.keys():
                if key != 'status' and key != 'name':
                    bot[key] = literal_eval(bot[key])
            bot_state[i] = bot
        return bot_state


    def get_character(player_id, players):
        for player in players:
            if player['id'] == player_id:
                return player

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    @socketio.on('start')
    def start():
        global game
        game = Game(len(bots), './maps/' + args.m)
        for bot in bots:
            new_id = game.get_available_id()
            bot.set_player_id(new_id)
            game.set_name(new_id, bot.get_name())

        command_factory = CommandFactory()
        while not game.game_over():
            for bot in bots:
                info = game.get_next_turn_info()
                player_turn = info['player_turn']

                if not game.bot_is_active(player_turn):
                    game.next_player()
                    continue

                players = parse_player_info(info)
                character = get_character(player_turn, players)
                other_players = get_other_players(player_turn, players)

                try:
                    que = Queue()
                    t = threading.Thread(target=run_bot_turn,
                                         args=(que, bot, info['game_state'], character, other_players))
                    t.start()
                    t.join(timeout=1.0)
                    if t.is_alive():
                        raise TimeoutError

                    command = que.get()
                    command = command_factory.create_command(command)
                    game.execute_command(command)
                except Exception as e:
                    print(e)
                    game.disconnect(player_turn)
                    game.next_player()

                emit('next turn', info, broadcast=True)

        print('The winner is {}'.format(game.get_winner()))


    socketio.run(app, port=5001)
