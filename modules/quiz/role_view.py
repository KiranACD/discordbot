import nextcord
from modules.quiz.quiz_view import QuizView
from modules.quiz.qadb import start_here


class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        
        start_button_response = None
        if button.custom_id == 'Start':
            question = start_here['1']['question']
            quiz_view = QuizView()
            start_button_response = await interaction.response.send_message(content=question, view = quiz_view, ephemeral=True)        

        elif button.custom_id == 'Reset':
            if start_button_response is not None:
                await start_button_response.delete()
            question = start_here['1']['question']
            quiz_view = QuizView()
            start_button_response = await interaction.response.send_message(content=question, view = quiz_view, ephemeral=True)
            
    @nextcord.ui.button(label='Start',
                        emoji="💖",
                        style=nextcord.ButtonStyle.green,
                        custom_id='Start')
    async def start_button(self, button, interaction):
        await self.handle_click(button, interaction)
    
    @nextcord.ui.button(label='Reset',
                        emoji="💖",
                        style=nextcord.ButtonStyle.danger,
                        custom_id='Reset')
    async def reset_button(self, button, interaction):
        await self.handle_click(button, interaction)