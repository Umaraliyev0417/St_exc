# https://edabit.com/challenge/S9KCN5kqoDbhNdKh5

def count_characters(lst):
    res = 0
    for x in lst:
        res += len(x)
    return res


print(count_characters([
  "###",
  "###",
  "###"
]))  # ➞ 9
print(count_characters([
  "22222222",
  "22222222",
]))  # ➞ 16

print(count_characters([
  "------------------"
]))  # ➞ 18

print(count_characters([]))  # ➞ 0

print(count_characters(["", ""]))  # ➞ 0
