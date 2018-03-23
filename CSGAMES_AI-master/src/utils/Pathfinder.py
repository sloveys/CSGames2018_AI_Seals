import networkx as nx
from networkx.algorithms.shortest_paths import astar_path

from src.symbols.MapSymbols import MapSymbols
from src.symbols.CharacterSymbols import CharacterSymbols
from src.symbols.ObjectSymbols import ObjectSymbols


class Pathfinder:

    def __init__(self):
        self.start = None
        self.goal = None
        self.game_map = None

    def set_game_state(self, game_state, players):
        self.game_map = self.parse_game_state(game_state)
        for player in players:
            location = player['location']
            self.game_map[location[0]][location[1]] = CharacterSymbols.CHARACTER
            base_location = player['base']
            self.game_map[base_location[0]][base_location[1]] = ObjectSymbols.BASE

    def get_next_direction(self, start, goal):
        self.start = start
        self.goal = goal
        graph = self.create_graph(self.game_map)
        path = astar_path(graph, start, goal)
        direction = self.convert_node_to_direction(path)
        return direction

    @staticmethod
    def convert_node_to_direction(path):
        if len(path) < 2:
            return None

        start = path[0]
        next = path[1]
        if start[1] == next[1] + 1:
            return 'W'

        elif start[1] == next[1] - 1:
            return 'E'

        elif start[0] == next[0] + 1:
            return 'N'

        else:
            return 'S'

    def create_graph(self, game_map):
        graph = nx.Graph()
        size_x = len(game_map[0])
        size_y = len(game_map)

        for y in range(size_y):
            for x in range(size_x):
                graph.add_node((y, x))

        for y in range(size_y - 1):
            for x in range(size_x - 1):
                symbol = game_map[y][x]
                if symbol.can_pass_through() or self._is_start_or_goal((y, x)):
                    right_symbol = game_map[y][x + 1]
                    if right_symbol.can_pass_through() or self._is_start_or_goal((y, x+1)):
                        graph.add_edge((y, x), (y, x+1))

                    bottom_symbol = game_map[y + 1][x]
                    if bottom_symbol.can_pass_through() or self._is_start_or_goal((y+1, x)):
                        graph.add_edge((y, x), (y+1, x))

        return graph

    def _is_start_or_goal(self, location):
        if location == self.start:
            return True
        elif location == self.goal:
            return True
        else:
            return False

    @staticmethod
    def create_symbol(character):
        if character in CharacterSymbols.get_symbols_value():
            return CharacterSymbols(character)

        elif character in ObjectSymbols.get_symbols_value():
            return ObjectSymbols(character)

        else:
            return MapSymbols(character)

    def parse_game_state(self, game_state):
        game_map = [[]]
        y = 0
        x = 0
        for character in game_state[:-1]:
            if character == '\n':
                game_map.append([])
                y += 1
                x = 0
            else:
                game_map[y].append(self.create_symbol(character))
                x += 1
        return game_map

