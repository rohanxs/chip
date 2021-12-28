from discord import Embed
from yahoostock.yahoo import get_open, get_previous_close

def get_day(args : list):
    stock_name = args[0].upper()

    try:
        opening_price = get_open(stock_name)
        closing_price = get_previous_close(stock_name)

        embed = Embed(
            title = "Day Stock Prices",
            description = f"Opening Price: `${opening_price}`\n" +
                          f"Closing Price: `${closing_price}`",
            color = 0x7842f5,
            url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
        )

    except:
        embed = Embed(
            title = "Stock Not Found",
            description = "The stock in your query was not found.",
            color = 0x7842f5
        )

    return embed