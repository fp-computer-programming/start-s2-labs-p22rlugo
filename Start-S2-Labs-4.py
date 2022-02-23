# Ryan Lugo: RJL 1/14/22

def double_every_other(lst):
    # For each itme in the list
    for ind, item in enumerate(lst):
        # If it matches 0 then
        if ind % 2 != 0:
            # Mult it by 2
            lst[ind] = item*2
    return lst