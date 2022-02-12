from discord.ext import commands
import random

class Random(commands.Cog, name='Random'):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):

        try:
            rolls = ''
            amount, die = dice.split('d')
            for _ in range(int(amount)):
                roll = random.randint(1, int(die))
                rolls += f'{roll} '
            await ctx.send(rolls)
        except ValueError:
            await ctx.send('Dice must be in format _d_ (2d6)')

def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))