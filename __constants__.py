from commands import get_help, get_invite, get_info, get_eval, get_graph, get_day, get_price, get_change

command_map = {
    'inv' : get_invite.get_invite,
    'hel' : get_help.get_help,
    'inf' : get_info.get_info,
    'eva' : get_eval.get_eval,
    'gra' : get_graph.get_graph,
    'day' : get_day.get_day,
    'pri' : get_price.get_price,
    'cha' : get_change.get_change
}

token = 'NzY4OTM1MTcxMzY1NjY2ODE2.X5Hsrg.YsAJLJGMiUfcnp_mnW1VYXSsVT0'