import os
from nextcord.ext import commands
from dotenv.main import load_dotenv# load environment variables if we are hosting it in an another platform.

def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    
    client = commands.Bot(command_prefix='$')

    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to discord.')
    
    @client.event
    async def on_message(ctx):
        if (ctx.content.startswith("Hello")):
            await ctx.channel.send(f'Hi {ctx.author.mention}')

        await client.process_commands(ctx)
    
    for folder in os.listdir('modules'):
        if os.path.exists(os.path.join('modules', folder, 'cog.py')):
            client.load_extension(f'modules.{folder}.cog')

    client.run(token)

if __name__ == '__main__':
    main()