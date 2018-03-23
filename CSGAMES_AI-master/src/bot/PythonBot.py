from src.bot.Bot import Bot
from src.symbols.ObjectSymbols import ObjectSymbols


class PythonBot(Bot):

    def __init__(self):
        super().__init__()

    def get_name(self):
        return 'Python'

    def turn(self, game_state, character_state, other_bots):
        super().turn(game_state, character_state, other_bots)
        goal = (1, 1)

        direction = self.pathfinder.get_next_direction(self.character_state['location'], goal)
        if direction:
            return self.commands.move(direction)
        else:
            return self.commands.idle()
