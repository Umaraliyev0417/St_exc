# https://edabit.com/challenge/MvgCxPkSgtQ8hQjwx

def remove_vowels(lst):
    vowel = "aeiou"
    res = ""
    for x in lst.lower():
        if x not in vowel:
            res += x
    return res

print(remove_vowels("I have never seen a thin person drinking Diet Coke."))