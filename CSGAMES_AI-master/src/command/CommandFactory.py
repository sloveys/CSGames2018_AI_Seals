from src.command.Rest import Rest
from src.command.Store import Store
from .Move import Move
from .Attack import Attack
from .Collect import Collect
from .Idle import Idle


class CommandFactory:

    @staticmethod
    def create_command(data):
        command = data['command']
        character_id = int(data['character_id'])

        if command == 'move':
            direction = data['direction']
            return Move(character_id, direction)

        if command == 'attack':
            direction = data['direction']
            return Attack(character_id, direction)

        if command == 'collect':
            return Collect(character_id)

        if command == 'store':
            return Store(character_id)

        if command == 'rest':
            return Rest(character_id)

        return Idle(character_id)
