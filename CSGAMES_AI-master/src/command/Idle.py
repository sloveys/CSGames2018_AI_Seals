from .Command import Command


class Idle(Command):

    def __init__(self, character_id):
        super().__init__(character_id)

    def execute(self, game_map, character):
        pass

    def log(self):
        print('Character {} did nothing.'.format(self.character_id))
