from discord import Embed

def get_help(args : list):
    embed = Embed(
        title = "Command List",
        description = (
            "`$help` : Displays a list of commands.\n"
            "`$inv` : Retrieves invite link to the bot.\n"
            "`$info <query>` : Returns information about the query.\n"
            "`$eval <stock>` : Checks profitability of a stock.\n"
            "`$graph <stock>` : Gives detailed graph of a stock's price history.\n"
            "`$price <stock>` : Returns the price of a certain stock.\n"
            "`$day <stock>` : Returns opening and closing prices on that day.\n"
            "`$chance <stock>` : Returns information about price change.\n"
        ),
        color = 0x7842f5
    )

    return embed