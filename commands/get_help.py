from discord import Embed

def get_help(args : list):
    embed = Embed(
        title = "Command List",
        description = (
            "`$help` : Displays a list of commands.\n"
            "`$inv` : Retrieves invite link to the bot.\n"
            "`$info <query>` : Returns information about the query.\n"
            "`$eval <stock>` : Checks profitability of a stock.\n"
            "`$graph <stock>` : Gives detailed graph the price of a stock.\n"
            "`$stock <stock>` : Returns information about a stock."
        ),
        color = 0x7842f5
    )

    return embed