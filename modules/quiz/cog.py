# from .role_view import RoleView
import nextcord
from nextcord.ext import commands
from modules.quiz import RoleView

class ButtonRolesCog(commands.Cog, name="Button"):

    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RoleView())
        print('button view added')
    
    @commands.command()
    @commands.is_owner()
    async def quiz(self, ctx: commands.Context):
        await ctx.send('Press start to begin the quiz!', view=RoleView())

def setup(bot: commands.Bot):
    bot.add_cog(ButtonRolesCog(bot))