# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import platform
import youtube_dl
from Token import token, pointless

startup_extensions = ["Music"]

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="PointlessBot by Q_#2980 using code from Habchy#1665 and YetiGuy", command_prefix="!", pm_help = False)


# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
    print('Created by Habchy#1665')
    return await client.change_presence(game=discord.Game(name='with himself')) #This is buggy, let us know if it doesn't work.
	
class General:
    """General Commands"""
    def __init__(self, bot):
        self.bot = bot

    # This is a basic example of a call and response command. You tell it do "this" and it does it.
    @client.command()
    async def ping(*args):
        """PONG"""
        await client.say(":ping_pong: Pong!")
    #	await asyncio.sleep(3)
    #	await client.say(":warning: This bot was created by **Habchy#1665**, it seems that you have not modified it yet. Go edit the file and try it out!")
    # After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.

    @client.command(pass_context=True)
    async def insult(ctx):
        """For when you're feeling a bit too good about yourself"""
        id = ctx.message.author.id
        if id == pointless:
            await client.say("Pointless you suck!")
        else:
            await client.say("ur mum gay")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, e))

client.run(token)

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.