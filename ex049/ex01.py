import random
yahtzee = {
    random.randint(1,6):'',
    random.randint(1,6):'',
    random.randint(1,6):'',
    random.randint(1,6):'',
    random.randint(1,6):''
}
print(yahtzee)
if(len(yahtzee.keys())==1):
    print("YAHTZEE!!!!")
else:
    print("No Yahtzee this time :(")