from discord import Embed
from yahoostock.yahoo import get_price as _get_price

def get_price(args : list):
    stock_name = args[0].upper()

    try:
        print(stock_name)
        price = _get_price(stock_name)
        
        embed = Embed(
            title = f"Price of Stock {stock_name}",
            description = f"Price: `${price}`\n",
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