
class Character:

    MAX_HEALTH = 100

    def __init__(self, character_id):
        self.id = character_id
        self.health = self.MAX_HEALTH
        self.points = 0
        self.carrying = 0
        self.location = (0, 0)
        self.base = (0, 0)
        self.status = 'alive'
        self.spawn_counter = 0
        self.name = 'Default'

    def damage(self, amount):
        if self.is_alive():
            if self.location != self.base:
                self.health -= amount

            if self.health <= 0:
                lost = self.carrying
                self.carrying = 0
                self.status = 'dead'
                self.spawn_counter = 10
                self.location = self.base
                return lost

        return 0

    def heal(self):
        self.health += 10
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH

    def store(self):
        if self.location == self.base:
            self.points += self.carrying
            self.carrying = 0

    def is_dead(self):
        return self.status == 'dead'

    def is_alive(self):
        return self.status == 'alive'

    def get_location(self):
        return self.location

    def get_id(self):
        return self.id

    def respawn(self):
        self.health = self.MAX_HEALTH
        self.location = self.base
        self.status = 'alive'

    def disconnect(self):
        self.location = self.base
        self.status = 'disconnected'

    def __str__(self):
        stats = {
            'id': str(self.id),
            'health': str(self.health),
            'carrying': str(self.carrying),
            'points': str(self.points),
            'location': str(self.location),
            'base': str(self.base),
            'status': self.status,
            'spawn': str(self.spawn_counter),
            'name': self.name
        }
        return str(stats)
