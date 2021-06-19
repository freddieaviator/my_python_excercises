
def bart_cheat_code_while(punishment_text,numb_of_repetition = 10):
    counter = 0
    while counter < numb_of_repetition:
        print(punishment_text + "\n")
        counter +=1

print(bart_cheat_code_while("Testing while"))

def bart_cheat_code_for(punishment_text,numb_of_repetition = 10):

    for i in range(numb_of_repetition):
        print(punishment_text + "\n")

print(bart_cheat_code_for("Testing for"))   