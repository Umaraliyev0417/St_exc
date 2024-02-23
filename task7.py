# https://edabit.com/challenge/rQkriLJBc9CbfRbJb

def index_of_caps(lst):
    res = []
    for x in lst:
        if x.isupper():
            res.append(lst.index(x))
    return res

print(index_of_caps("eDaBiT"))