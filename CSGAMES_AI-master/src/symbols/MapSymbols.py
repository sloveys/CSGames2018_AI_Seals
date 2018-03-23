from enum import Enum, unique


@unique
class MapSymbols(Enum):

    GRASS = '0'
    TREE = '1'
    RIVER = '2'

    def can_pass_through(self):
        return self is MapSymbols.GRASS