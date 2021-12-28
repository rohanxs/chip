from discord import Embed, Color
from wikipedia import search, summary

def get_info(args : list):
    for i in range(len(args)):
        args[i] += " "
    query = "".join(args)

    try:
        search_result = str(search(query)[0])

        embed = Embed(
            title = "Wikipedia Information",
            description = summary(search_result),
            color = 0x7842f5,
            url = f"https://en.wikipedia.org/wiki/{search_result.replace(' ', '_')}"
        )

    except:
        embed = Embed(
            title = "Query Error",
            description = "No such article found!",
            color = 0x7842f5
        )

    return embed
