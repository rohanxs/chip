from yahoostock.yahoo import *
from discord import Embed, Color

def get_stock(args : list):
    stock_name = args[0].upper()

    try:
        _price, _change, _per_change, _open, _prev_close = (
            round(get_price(stock_name), 2),
            round(get_change(stock_name), 2),
            round(get_percent_change(stock_name), 2),
            round(get_open(stock_name), 2),
            round(get_previous_close(stock_name), 2)
        )

        embed = Embed(
            title = f"Information About Stock `{stock_name}`",
            description = (
                f"\nStock Price: `${_price}`\n"
                f"Price Change: `${_change}`\n"
                f"Percent Price Change: `{_per_change}%`\n"
                f"Opening Price: `${_open}`\n"
                f"Previous Closing Price: `${_prev_close}`"
            ),
            color = 0x7842f5
        )

    except:
        embed = Embed(
            title = "Stock Not Found",
            description = "The stock in your query was not found.",
            color = Color.red()
        )

    return embed