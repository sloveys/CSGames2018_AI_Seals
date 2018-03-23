from .Command import Command


class Collect(Command):

    def __init__(self, character_id):
        super().__init__(character_id)
        self.collected_object = None

    def execute(self, game_map, character):
        self.collected_object = game_map.collect(character.get_location())
        self.collected_object.update(character)

    def log(self):
        print('Character {} collected {}.'.format(self.character_id, self.collected_object))
