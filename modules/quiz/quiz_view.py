import nextcord
from nextcord.ext import commands
from modules.quiz.qadb import start_here

class MyButton(nextcord.ui.Button):
    def __init__(self, label, style, custom_id, view_instance):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.view_instance = view_instance
    
    async def callback(self, interaction):
        await self.view_instance.option_button(interaction, self.custom_id)
        


class QuizView(nextcord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)
        self.count = 1
        self.options = start_here[str(self.count)]['options']
        self.questions_done = 0
        self.correct_answers = 0
        self.buttons = []

        for _ in range(len(self.options)):
            button = MyButton(self.options[0],
                              nextcord.ButtonStyle.primary,
                              self.options[_],
                              self)
            self.buttons.append(button)
            self.add_item(button)
    
    async def handle_click(self, interaction, custom_id):

        if self.count <= len(start_here):
            answer = start_here[str(self.count)]['answer']
            if custom_id == answer:
                self.correct_answers += 1
            self.questions_done += 1
            self.count += 1
            question = f'{self.count}. Question'
            self.remove_item(self.button)
            self.option_label = f'first choice {self.count}'
            self.button = MyButton(self.option_label,
                                nextcord.ButtonStyle.primary,
                                f'{self.count}_first choice',
                                self)
            self.add_item(self.button)
            
            await interaction.response.edit_message(content=question, view=self)
        else:
            if self.correct_answers == self.questions_done:
                role = nextcord.utils.get(interaction.user.guild.roles, name='Newb')
                await interaction.user.add_roles(role)
                result = f'Quiz Ended. Congrats you have been promoted to {role.name}'
                await interaction.response.edit_message(content=result, view=None)
            else:
                result = f'Quiz Ended. You did not answer all questions corretly. Try again!'
                await interaction.response.edit_message(content=result, view=None)


    async def option_button(self, interaction, custom_id):
        await self.handle_click(interaction, custom_id)