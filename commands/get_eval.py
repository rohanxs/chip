from discord import Embed, Color
from requests import get

def get_eval(args : list):
    stock_name = args[0].upper()

    try:
        scraped_text = get(
            f'https://money.cnn.com/quote/forecast/forecast.html?symb={stock_name}'
        ).text
        _ = scraped_text.index('The median estimate represents a ')

    except:
        return Embed(
            title = "Stock Not Found",
            description = "The stock in your query was not found.",
            color = 0x7842f5
        )

    evaluation = round(float(scraped_text[
        _+28 : _+128
    ].split('">')[1].split('%')[0])/100, 4)

    if (evaluation < 0):
        description = (
            f"The `{stock_name}` stock has an evaluation score of `{evaluation}`, "
            "meaning the stock doesn't show any signs of rising in the near future."
        )
        color = Color.red()

    elif (evaluation < 0.33):
        description = (
            f"The `{stock_name}` stock has an evaluation score of `{evaluation}`, "
            "meaning the stock may possibly rise in the near future."
        )
        color = Color.blue()

    else:
        description = (
            f"The `{stock_name}` stock has an evaluation score of `{evaluation}`, "
            "meaning the stock will almost certainly rise in the near future."
        )
        color = Color.green()

    return Embed(
        title = "Stock Evaluation",
        description = description,
        color = color,
        url = f"https://money.cnn.com/quote/forecast/forecast.html?symb={stock_name}"
    )