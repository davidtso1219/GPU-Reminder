import discord
import os
from keep_alive import keep_alive
from discord.utils import get

client = discord.Client()

# Ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def getChannel(ctx, name):
    """
    Get a specific channel with the name of "name."
    """
    for channel in ctx.guild.channels:
        if (channel.name == name):
            return channel
    

@client.event
async def on_message(ctx):
    """
    This event handler will check if there is an announcement from InStockAlert_DataLover. If so, the bot will ping the role, miner, in the general channel. 
    """

    # check if the message is in the announcement channel and check the author
    if ctx.channel.name != "announcement" or ctx.author.name != "InStockAlert_DataLover #rtx3070":
        return
    
    # get "general" channel, and announcement channel
    general = getChannel(ctx, 'general')
    announcement = getChannel(ctx, 'announcement')
    
    # get the minor role
    miner = get(ctx.guild.roles, name="miner")

    # send the message to mention minors and 
    await general.send(content=f"{miner.mention}\nHead up! New Updates in {announcement.mention} channel")
    return

if __name__ == "__main__":
    keep_alive()
    token = os.environ.get("TOKEN")
    client.run(token)
