def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]}")

def summon_captain_planet(lists):
    return [f"{list.title()}!" for list in lists]

def long_planeteer_calls(lists):
    for list in lists:
        if len(list) > 4:
            return True

    return False


def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    
    for string in strings:
        if string in cheeses:
            return f"{string}"
        else:
            None
    
    
    
    # cheeses = {"cheddar", "gouda", "camembert"}
    # lists = set(strings)
    
    # return f"{cheeses & lists}"