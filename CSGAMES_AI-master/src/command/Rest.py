from .Command import Command


class Rest(Command):

    def __init__(self, character_id):
        super().__init__(character_id)

    def execute(self, game_map, character):
        character.heal()

    def log(self):
        print('Character {} healed himself.'.format(self.character_id))
