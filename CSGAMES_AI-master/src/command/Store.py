from .Command import Command


class Store(Command):

    def __init__(self, character_id):
        super().__init__(character_id)
        self.points = 0

    def execute(self, game_map, character):
        self.points = character.carrying
        character.store()

    def log(self):
        print('Character stored {} points.'.format(self.points))
