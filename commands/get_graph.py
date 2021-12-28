from discord import Embed
from requests import get

def get_graph(args : list):
    stock_name = args[0].upper()

    try:
        get(
            f'https://money.cnn.com/quote/forecast/forecast.html?symb={stock_name}'
        ).text.index('The median estimate represents a ')
    
    except:
        embed = Embed(
            title = "Stock Not Found",
            description = "The stock in your query was not found.",
            color = 0x7842f5
        )
        embed.set_author(
            name = "Chip",
            icon_url = "https://media.discordapp.net/attachments/685653019856994381/899826225227378768/stock.jpg"
        )
        embed.set_thumbnail(
            url = "https://media.discordapp.net/attachments/685653019856994381/899826225227378768/stock.jpg"
        )

        return embed

    chart = f"https://stockcharts.com/c-sc/sc?s={stock_name.lower()}&p=D&b=5&g=0&i=0"

    embed = Embed(
        title = "Stock Graph",
        description = f"Graph for stock `{stock_name}` over the past six months:",
        color = 0x7842f5,
        url = chart
    )
    embed.set_image(
        url = chart
    )
    embed.set_author(
            name = "Chip",
            icon_url = "https://media.discordapp.net/attachments/685653019856994381/899826225227378768/stock.jpg"
        )
    embed.set_thumbnail(
        url = "https://media.discordapp.net/attachments/685653019856994381/899826225227378768/stock.jpg"
    )

    return embed