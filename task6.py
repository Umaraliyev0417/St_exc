# https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma

def is_isogram(lst):
    for x in lst.lower():
        if lst.count(x) > 1:
            return False

    return True

print(is_isogram("Algorism"))

