from __constants__ import command_map, token

import discord
client = discord.Client()

@client.event 
async def on_ready():
    await client.wait_until_ready()

    print(f'Chip is up and running!')

@client.event 
async def on_message(message): 
    await client.wait_until_ready()
    
    if not (message.content.startswith('$')): return

    command = message.content.split(' ')[0][1:4]
    try: args = message.content.split(' ')[1:]
    except: args = []

    embed = command_map[command](args)  
    embed.set_author(
        name = message.author.name,
        icon_url = message.author.avatar_url
    )
    embed.set_thumbnail(
        url = "https://media.discordapp.net/attachments/685653019856994381/899826225227378768/stock.jpg"
    )

    await message.channel.send(embed = embed)

client.run(token)