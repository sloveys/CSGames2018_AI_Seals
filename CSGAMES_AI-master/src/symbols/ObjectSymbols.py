from enum import Enum, unique


@unique
class ObjectSymbols(Enum):

    BASE = 'B'
    JUNK = 'J'
    SPIKE = 'S'

    @staticmethod
    def get_symbols_value():
        values = []
        for _, member in ObjectSymbols.__members__.items():
            values.append(member.value)
        return values

    def can_pass_through(self):
        return self is not ObjectSymbols.BASE
