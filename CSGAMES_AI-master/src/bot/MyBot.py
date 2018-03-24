from src.bot.Bot import Bot
from src.symbols.ObjectSymbols import ObjectSymbols


class MyBot(Bot):
    state = 0

    def __init__(self):
        super().__init__()
        self.state = 0;

    def get_goal(self, game_state, search, char_location):
        if (game_state == None or search == None or char_location == None):
            return None
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
            tempLen = self.get_distence(allOfSearch[i], char_location)
            if (tempLen == None):
                continue
            if (minLoc == -1):
                minLoc = i
                minLen = tempLen
            elif (tempLen < minLen):
                minLoc = i
                minLen = tempLen
        if (minLoc == -1):
            return None
        return allOfSearch[minLoc]

    def get_distence(self, a_loc, b_loc):
        if (a_loc == None or b_loc == None):
            return None
        return ((a_loc[0] - b_loc[0])**2 + (a_loc[1] - b_loc[1])**2)**0.5

    def get_name(self):
        # Find a name for your bot
        return 'Seals Meals'

    def adjacent_loc(self, a_loc, b_loc):
        if (a_loc == None or b_loc == None):
            return None
        if (a_loc[0] == b_loc[0]):
            if (a_loc[1] == b_loc[1]-1):
                return 'E'
            elif (a_loc[1] == b_loc[1]+1):
                return 'W'
            elif (a_loc[1] == b_loc[1]):
                return '0'
            else:
                return None
        if (a_loc[1] == b_loc[1]):
            if (a_loc[0] == b_loc[0]-1):
                return 'S'
            elif (a_loc[0] == b_loc[0]+1):
                return 'N'
            elif (a_loc[0] == b_loc[0]):
                return '0'
            else:
                return None
        return None

    def turn(self, game_state, character_state, other_bots):
        super().turn(game_state, character_state, other_bots)
        char_location = self.character_state['location']
        char_base = self.character_state['base']
        char_carry = self.character_state['carrying']
        if (char_location == None):
            return self.commands.idle()

        if (char_location == char_base):
            self.state = 0
            if (self.character_state['carrying'] > 0):
                return self.commands.store()
            elif (self.character_state['health'] < 100):
                return self.commands.rest()

        for bot in other_bots:
            bot_dir = self.adjacent_loc(char_location, bot['location'])
            if not (bot_dir == None or bot_dir == '0'):
                if (char_carry > 0):
                    self.state = 1
                    break
                if (self.adjacent_loc(bot['location'], bot['base']) == None):
                    return self.commands.attack(bot_dir)

        if (char_carry == 0):
            goal = self.get_goal(game_state, 'J', char_location)
            if (goal == char_location):
                return self.commands.collect()
        elif (char_carry < 300 and self.state == 0):
            return self.commands.collect()
        else:
            goal = char_base

        if (goal == None or char_location == None):
            return self.commands.idle()

        direction = self.pathfinder.get_next_direction(char_location, goal)
        if direction:
            return self.commands.move(direction)
        else:
            return self.commands.idle()
