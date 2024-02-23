# https://edabit.com/challenge/m9bcZKy4niMmsg3JX

def society_name(lst):
    a = ""
    for x in sorted(lst):
        a += x[0]
    return a

print(society_name(["Adam", "Sarah", "Malcolm","Yuj","Badf"]))