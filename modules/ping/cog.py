from nextcord.ext import commands

class Ping(commands.Cog, name='Ping'): #name is the name of the category
    '''Receives ping commands'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        '''Checks for response from bot''' 
        await ctx.send('pong')

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))