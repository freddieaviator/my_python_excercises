import random

dice = [1,2,3,4,5,6]
n_dices = 5

rand_dices = random.choices(dice,weights=None,cum_weights=None,k = n_dices)

if(rand_dices[0] == rand_dices[1] == rand_dices[2] == rand_dices[3] == rand_dices[4]):
    print("YAHTZEE!!!!")
else:
    print("No Yahtzee this time :(")

print(f"""Min value was: {min(rand_dices)} and Max value was: {max(rand_dices)}.
Sorted list of dices: {sorted(rand_dices)}""")