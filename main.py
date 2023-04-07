import os
import discord
from discord.ext import commands
from keep_alive import keep_alive 
intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)
my_secret = os.environ['Token']

@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def doubt(ctx, arg):
    channelID = 1093521032402452561  # Replace with the ID of the channel to post the embedded message
    link = f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}"
    channel = client.get_channel(channelID)
    embed = discord.Embed(title='New Doubt!',
                          description=arg,
                          colour=discord.Colour.blue())
    embed.add_field(name='Channel', value=ctx.channel)
    embed.add_field(name='Author', value=ctx.author.mention)
    embed.add_field(name='Link', value=link)

    message = await channel.send(embed=embed)
    msg_channel = client.get_channel(ctx.channel.id)
    jump_url = message.jump_url.replace(str(channelID), str(msg_channel.id))
    await message.edit(embed=discord.Embed(title='New Doubt!',
                                           description=arg,
                                           colour=discord.Colour.blue())
                       .add_field(name='Channel', value=ctx.channel)
                       .add_field(name='Author', value=ctx.author.mention)
                       .add_field(name='Link', value=jump_url))
  
keep_alive()
client.run(my_secret)

#  Add your bot token here to use it in your channel