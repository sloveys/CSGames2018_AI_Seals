from src.bot.Bot import Bot


class MyBot(Bot):

    def __init__(self):
        super().__init__()

    def get_name(self):
        # Find a name for your bot
        return 'My bot'

    def turn(self, game_state, character_state, other_bots):
        # Your bot logic goes here
        super().turn(game_state, character_state, other_bots)
        return self.commands.idle()
