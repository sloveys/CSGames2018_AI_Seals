from src.object.Junk import Junk
from src.symbols.MapSymbols import MapSymbols
from src.symbols.ObjectSymbols import ObjectSymbols
from copy import deepcopy
from random import choice


class Map:

    def __init__(self, map_file):
        self.map = []
        self.objects = {}
        self.characters = {}
        self.base = {}
        self.junk = {}
        for symbols in ObjectSymbols:
            self.objects[symbols.value] = []

        self._generate(map_file)

    def _generate(self, map_file):
        file = open(map_file)
        for i, line in enumerate(file):
            self.map.append([])
            for j, symbol in enumerate(line.replace('\n', '')):
                symbol = self._parse_symbol(symbol, (i, j))
                self.map[i].append(symbol)
        file.close()

    def _parse_symbol(self, symbol, location):
        if symbol in ObjectSymbols.get_symbols_value():
            self.objects[symbol].append(location)
            if symbol == ObjectSymbols.JUNK.value:
                self.junk[location] = Junk()

            return MapSymbols.GRASS.value
        else:
            return symbol

    def add_character(self, character):
        spawn_locations = self.objects[ObjectSymbols.BASE.value]
        selected_spawn = choice(spawn_locations)
        character.location = selected_spawn
        character.base = selected_spawn
        self.base[character.get_id()] = selected_spawn
        self.objects[ObjectSymbols.BASE.value].remove(selected_spawn)
        self.characters[character.get_id()] = character
        return selected_spawn

    def get_empty_locations(self):
        empty_locations = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self._check_is_valid_location((i, j)):
                    empty_locations.append((i, j))
        return empty_locations

    def collect(self, location):
        game_object = self.get_object_at_location(location)
        if game_object is ObjectSymbols.JUNK:
            return self.junk[location]

    def get_object_at_location(self, location):
        for object_type in self.objects.keys():
            possible_locations = self.objects[object_type]
            if location in possible_locations:
                return ObjectSymbols(object_type)

        return None

    def get_character_at_location(self, location):
        for character_id in self.characters.keys():
            if self.characters[character_id].get_location() == location:
                return self.characters[character_id]

    def _get_other_players_base(self, character_id):
        character = self.characters[character_id]
        other_base = []
        for base in self.base.values():
            if base != character.base:
                other_base.append(base)
        return other_base

    def _check_is_valid_location(self, character_id, location):
        if self.get_character_at_location(location):
            return False

        if location in self._get_other_players_base(character_id):
            return False

        if self.get_object_at_location(location):
            return ObjectSymbols(self.get_object_at_location(location)).can_pass_through()

        else:
            y, x = location
            return MapSymbols(self.map[y][x]).can_pass_through()

    def update_character_location(self, character_id, new_location):
        if self._check_is_valid_location(character_id, new_location):
            self.characters[character_id].location = new_location

    def remove_character(self, character_id):
        self.characters.pop(character_id)

    def get_final_map(self):
        final_map = deepcopy(self.map)
        for symbol in self.objects.keys():
            for i, j in self.objects[symbol]:
                final_map[i][j] = symbol

        return final_map

    def __str__(self):
        final_map = self.get_final_map()
        printed_map = ''
        for i in range(len(final_map)):
            for j in range(len(final_map[i])):
                printed_map += final_map[i][j]
            printed_map += '\n'
        return printed_map


if __name__ == '__main__':
    competition_map = Map('../maps/map1')
    competition_map.add_character('1')
    competition_map.update_character_location('1', (3, 5))
    print(competition_map)