import nextcord


class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.count = 0
    
    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        self.count += 1
        await interaction.response.edit_message(content=f'Edited_{self.count}', view=self)
        

    @nextcord.ui.button(label='Subscriber',
                        emoji="💖",
                        style=nextcord.ButtonStyle.primary,
                        custom_id='question_answer')
    async def subscriber_button(self, button, interaction):
        await self.handle_click(button, interaction)