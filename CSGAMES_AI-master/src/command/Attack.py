from .Command import Command


class Attack(Command):

    def __init__(self, character_id, direction):
        super().__init__(character_id)
        self.attack_direction = direction

    def execute(self, game_map, character):
        attack_location = self.get_aimed_location(character.get_location(), self.attack_direction)
        attacked_character = game_map.get_character_at_location(attack_location)
        if attacked_character:
            character.carrying += attacked_character.damage(10)

    def log(self):
        print('{} attacked {}'.format(self.character_id, self.attack_direction))
