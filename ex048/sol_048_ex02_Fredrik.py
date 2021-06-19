import random

target_number = int(input("Enter the target number: "))
allowed_attempts = int(input("Enter number of allowed attempts: "))

print(chr(27) + "[2J")  #Clear Terminal

counter = 0

while counter < allowed_attempts:
    print(f"You have {allowed_attempts-counter} attempts remaining.")
    guess = int(input("Guess the number: "))
    if(guess == target_number):
        print(f"{guess} was the correct number! Congratulations!")
        break
    else:
        if(guess < target_number):
            print(f"Unfortunately {guess} was too small!")
        else:
            print(f"Unfortunately {guess} was too large!")
        counter += 1

if counter == allowed_attempts:
    print(f"""You have used all your {allowed_attempts} attempts.
The correct number was {target_number}!
Better luck next time!""")