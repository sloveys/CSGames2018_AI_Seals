class Commands:

    def __init__(self, player_id):
        self.player_id = player_id

    def attack(self, direction):
        data = {
            'command': 'attack',
            'character_id': str(self.player_id),
            'direction': direction
        }
        return data

    def collect(self):
        data = {
            'command': 'collect',
            'character_id': str(self.player_id)
        }
        return data

    def idle(self):
        data = {
            'command': 'idle',
            'character_id': str(self.player_id)
        }
        return data

    def move(self, direction):
        data = {
            'command': 'move',
            'character_id': str(self.player_id),
            'direction': direction
        }
        return data

    def rest(self):
        data = {
            'command': 'rest',
            'character_id': str(self.player_id)
        }
        return data

    def store(self):
        data = {
            'command': 'store',
            'character_id': str(self.player_id)
        }
        return data