class Command:

    def __init__(self, character_id):
        self.character_id = character_id

    def get_id(self):
        return self.character_id

    def execute(self, game_map, character):
        raise NotImplementedError

    def log(self):
        raise NotImplementedError

    @staticmethod
    def get_aimed_location(initial_location, direction):
        new_y, new_x = initial_location
        if direction == 'N':
            new_y -= 1
        elif direction == 'S':
            new_y += 1
        elif direction == 'E':
            new_x += 1
        elif direction == 'W':
            new_x -= 1

        return new_y, new_x
