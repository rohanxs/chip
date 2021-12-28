from discord import Embed
from yahoostock.yahoo import get_change as _get_change
from yahoostock.yahoo import get_percent_change

def get_change(args : list):
    stock_name = args[0].upper()

    try:
        change = _get_change(stock_name)
        percent_change = get_percent_change(stock_name)

        embed = Embed(
            title = "Stock Price Change",
            description = f"Total Change: `${round(change, 2)}`\n" +
                          f"Percent Change: `{percent_change}%`",
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