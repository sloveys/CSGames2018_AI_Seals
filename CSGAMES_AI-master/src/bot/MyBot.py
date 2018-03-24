from src.bot.Bot import Bot
from src.symbols.ObjectSymbols import ObjectSymbols


class MyBot(Bot):

    def __init__(self):
        super().__init__()
        self.state = 0;

    def get_goal(self, game_state, search, char_location):
        y = 0
        x = 0
        found = False
        allOfSearch = []
        for c in game_state:
            if c == '\n':
                y = y + 1
                x = 0
            elif c == search:
                if not (x == 0 or y == 0):
                    allOfSearch.append((y,x-1))
            x = x + 1
        if (len(allOfSearch) == 0):
            return None
        minLen = None
        minLoc = -1
        for i in range(len(allOfSearch)):
            tempLen = ((allOfSearch[i][0] - char_location[0])**2 + (allOfSearch[i][1] - char_location[1])**2)**0.5
            if (minLoc == -1):
                minLoc = i
                minLen = tempLen
            elif (tempLen < minLen):
                minLoc = i
                minLen = tempLen
        if (minLoc == -1):
            return None
        return allOfSearch[minLoc]


    def get_name(self):
        # Find a name for your bot
        return 'Seals Meals'

    def turn(self, game_state, character_state, other_bots):
        super().turn(game_state, character_state, other_bots)
        char_location = self.character_state['location']
        char_base = self.character_state['base']
        if (char_location == base):
            if (self.character_state['carrying'] > 0):
                self.commands.store()

        if (self.character_state['carrying'] == 0):
            goal = self.get_goal(game_state, 'J', char_location)
            if (goal == char_location):
                return self.commands.collect()
        elif (self.character_state['carrying'] < 100):
            return self.commands.collect()
        else:
            goal = char_base

        if (goal == None):
            return self.commands.idle()

        direction = self.pathfinder.get_next_direction(char_location, goal)
        if direction:
            return self.commands.move(direction)
        else:
            return self.commands.idle()
