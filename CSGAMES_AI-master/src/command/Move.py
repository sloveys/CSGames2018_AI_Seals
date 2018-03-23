from src.symbols.ObjectSymbols import ObjectSymbols
from .Command import Command
from random import randrange


class Move(Command):

    def __init__(self, character_id, direction):
        super().__init__(character_id)
        self.direction = direction

    def execute(self, game_map, character):
        new_location = self.get_aimed_location(character.get_location(), self.direction)

        if game_map.get_object_at_location(new_location) is ObjectSymbols.SPIKE:
            character.damage(randrange(5, 15))

        game_map.update_character_location(self.character_id, new_location)

    def log(self):
        print('Character {} moved {}'.format(self.character_id, self.direction))
