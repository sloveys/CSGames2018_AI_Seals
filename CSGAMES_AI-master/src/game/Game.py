from .Character import Character

from src.game.Map import Map


class Game:

    def __init__(self, number_of_characters, map_name, max_turns=100):

        self.number_of_characters = number_of_characters
        self.available_ids = [x for x in range(number_of_characters)]
        self.map_name = map_name
        self.max_turns = max_turns
        self.turn_number = 0

        self.map = Map(map_name)
        self.characters = []

        self._init_world()

        self.current_player_turn = 0

        self.game_history = []

    def _init_world(self):
        self._add_characters()

    def _add_characters(self):
        for i in range(self.number_of_characters):
            new_character = Character(i)
            self.characters.append(new_character)
            self.map.add_character(new_character)

    def disconnect(self, player_id):
        self.characters[player_id].disconnect()
        self.map.remove_character(player_id)

    def bot_is_active(self, player_id):
        return self.characters[player_id].status != 'disconnected'

    def get_next_turn_info(self):
        infos = {
            'game_state': str(self.map),
            'player_turn': self.get_current_player_turn(),
            'player_info': str([str(self.characters[i]) for i in range(self.number_of_characters)])
        }
        self.game_history.append(infos)
        return infos

    def set_name(self, player_id, name):
        self.characters[player_id].name = name

    def get_available_id(self):
        if len(self.available_ids) != 0:
            return self.available_ids.pop(0)
        else:
            return 'No ids available'

    def get_current_player_turn(self):
        return self.current_player_turn

    def execute_command(self, command):
        character = self.characters[command.get_id()]
        if character.is_alive():
            command.execute(self.map, character)
            print(command.log())
        else:
            character.spawn_counter -= 1
            if character.spawn_counter == 0:
                character.respawn()
                print('Character {} respawned'.format(command.get_id))
            else:
                print('{} is dead, {} turn remaining'.format(command.get_id(), character.spawn_counter))
        self.next_player()

    def next_player(self):
        self.current_player_turn += 1
        self.current_player_turn %= len(self.characters)

        if self.current_player_turn == 0:
            self. end_turn()

    def end_turn(self):
        self.turn_number += 1

    def get_winner(self):
        winner = [self.characters[0]]
        for character in self.characters[1:]:
            if character.points == winner[0].points:
                winner.append(character)

            if character.points > winner[0].points:
                winner = [character]

        return [str(x) for x in winner]

    def game_over(self):
        player_left = 0
        for i in range(len(self.characters)):
            if self.bot_is_active(i):
                player_left += 1
        return self.turn_number >= 1000 or player_left <= 1

if __name__ == '__main__':

    g = Game(2, '../maps/map1')
