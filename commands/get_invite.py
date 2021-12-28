from discord import Embed

def get_invite(args : list):
    embed = Embed(
        title = "Invite Link",
        description = "Invite Chip to your own server!",
        color = 0x7842f5,
        url = "https://discord.com/api/oauth2/authorize?client_id=899803016419487794&permissions=8&scope=bot"
    )

    return embed