from yahoostock.yahoo import *
from discord import Embed, Color

def get_stock(args : list):
    stock_name = args[0].upper()

    try:
        _price, _change, _per_change, _open, _prev_close = (
            get_price(stock_name),
            get_change(stock_name),
            get_percent_change(stock_name),
            get_open(stock_name),
            get_previous_close(stock_name)
        )

        embed = Embed(
            title = "Stock Information",
            description = (
                f"Stock Price: `${_price}`\n"
                f"Change in Price: `${_change}`\n"
                f"Percent Change in Price: `%{_per_change}`\n"
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