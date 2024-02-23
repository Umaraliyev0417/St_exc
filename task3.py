# https://edabit.com/challenge/EFwDXErjDywXp56WG

def is_in_order(lst):
    if sorted(lst) == list(lst):
        return True
    else:
        return False

print(is_in_order("abc"))