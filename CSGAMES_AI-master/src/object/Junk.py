from random import randrange, gauss


class Junk:

    def __init__(self):
        self.mu = randrange(5, 20)
        self.sigma = randrange(1, 10)
        self.last_amount = 0

    def update(self, character):
        amount = gauss(self.mu, self.sigma)
        if amount > 0:
            amount = int(amount)
            self.last_amount = amount
            character.carrying += amount

        self.last_amount = 0

    def __str__(self):
        return '{} points'.format(self.last_amount)
