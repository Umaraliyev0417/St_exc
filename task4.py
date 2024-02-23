# https://edabit.com/challenge/EfEpbcGjXQYDFcdxF

def filter_list(lst):
    a = []
    for x in lst:
        if type(x) == int:
            a.append(x)
        else:
            pass
    return a


print(filter_list([1, 2, 3, "a", "b", 4]))