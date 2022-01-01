from commands import get_help, get_invite, get_info, get_eval, get_graph, get_stock

command_map = {
    'inv' : get_invite.get_invite,
    'hel' : get_help.get_help,
    'inf' : get_info.get_info,
    'eva' : get_eval.get_eval,
    'gra' : get_graph.get_graph,
    'sto' : get_stock.get_stock
}

token = '<token>'