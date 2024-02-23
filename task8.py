# https://edabit.com/challenge/4Agr8CTY7x2rAhh5n

def alphabet_soup(lst):
    res = ""
    text = list(lst)
    text.sort()
    return res.join(text)

print(alphabet_soup("edabit"))