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
    async def roles(self, ctx: commands.Context):
        await ctx.send('Click a button to add or remove a role', view=RoleView())

def setup(bot: commands.Bot):
    bot.add_cog(ButtonRolesCog(bot))
# class QuizButton(discord.ui.Button):

#     def __init__(self, answer_option: str, question: str):
#         '''Button for the quiz answers.'''

#         super().__init__(label=answer_option, style=discord.enums.ButtonStyle.primary, custom_id=f'{question}_{answer_option}')

#     async def callback(self, interaction: discord.Interaction):
#         '''This function will be called any time a user clicks on this button'''

#         user = interaction.user
#         answer = self.custom_id.split('_')[-1]


# class Quiz():
#     '''Creates buttons that assign roles'''

#     def __init__(self, bot: commands.Bot):
#         self.bot = bot
    
#     @commands.Cog.listener()
#     async def on_ready(self):
#         '''Called when cog is loaded'''

#         pass



# class LaunchQuiz():

#     def __init__(self, bot):
#         self.bot = bot
    
#     #embed with button that will launch the quiz
