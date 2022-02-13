import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os
import redis


class ReadEmailRegister(commands.Cog, name='Read Email'): #name is the name of the category
    '''Receives ping commands'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.r = redis.Redis(decode_responses=True)
        load_dotenv()
        self.channel_id = int(os.getenv("REGISTRATION_CHANNEL_ID"))
    
    @commands.command()
    async def email(self, ctx: commands.Context, email: str):
        '''Reads email from user for registration'''

        user = ctx.author
        channel_check = 0
        #check if channel id matches the registration channel id
        if ctx.channel.id == self.channel_id:
            channel_check = 1
        
        if channel_check == 0:
            await user.send(f'{user.mention} Send email from #register-yourself channel')
            await ctx.message.delete()
            return

        email_found_in_db = 0
        print(self.r.smembers('subscriptions'))
        print(email)
        print(email in self.r.smembers('subscriptions'))
        #check if email in thinkific db
        if self.r.sismember('subscriptions', email):
            email_found_in_db = 1
        
        if email_found_in_db == 0:
            await user.send(f'{user.mention} Please wait 5 minutes before trying again.')
            await ctx.message.delete()
            return

        email_in_use = 0
        if self.r.get(f'{email}_duid') is not None:
            email_in_use = 1
        
        if email_in_use == 1:
            await user.send(f'{user.mention} Email is already in use.')
            await ctx.message.delete()
            return
        
        print('Reached role assignment.')

        role = nextcord.utils.get(user.guild.roles, name='Active')

        await user.add_roles(role)

        self.r.set(f'{email}_duid', user.id)
        roles = user.roles
        for role in roles:
            self.r.sadd(f'{email}_{user.id}_role_name', role.name)
        
        await user.send(f'{user.mention} You are registered. Proceed to the #start-here channel.')
        await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(ReadEmailRegister(bot))