from enum import Enum, unique


@unique
class CharacterSymbols(Enum):
    CHARACTER = 'C'

    @staticmethod
    def get_symbols_value():
        values = []
        for _, member in CharacterSymbols.__members__.items():
            values.append(member.value)
        return values

    def can_pass_through(self):
        return False
