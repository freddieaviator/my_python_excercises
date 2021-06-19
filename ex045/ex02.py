import random

dice = [1,2,3,4,5,6]
n_dices = 5
counter = 0
while True:
    rand_dices = random.choices(dice,weights=None,cum_weights=None,k = n_dices)
    counter += 1
    if(rand_dices[0] == rand_dices[1] == rand_dices[2] == rand_dices[3] == rand_dices[4]):
        print("YAHTZEE!!!!")
        print(f"""Min value was: {min(rand_dices)} and Max value was: {max(rand_dices)}.
        Sorted list of dices: {sorted(rand_dices)}""")
        print(counter)
        break
    else:
        print("No Yahtzee this time :(")

    #print(f"""Min value was: {min(rand_dices)} and Max value was: {max(rand_dices)}.
    #Sorted list of dices: {sorted(rand_dices)}""")