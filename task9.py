# https://edabit.com/challenge/HpqLxNqqRvMQoz8ME

def double_char(lst):
    res = ""
    for x in lst:
        res += x+x
    return res


print(double_char("String"))