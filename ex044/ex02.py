import random
yahtzee = {
    'a' : random.randint(1,6),
    'b' : random.randint(1,6),
    'c' : random.randint(1,6),
    'd' : random.randint(1,6),
    'e' : random.randint(1,6)
}
print(yahtzee)
if(a == b == c == d == e):
    print("YAHTZEE!!!!")
else:
    print("No Yahtzee this time :(")