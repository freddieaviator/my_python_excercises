

first_number = input("Input first number: ")
second_number = input("Input second number: ")
operator = input("Input type of operator (+,-,*,/): ")
special_character = "+-*/"

if(not first_number.isalpha() and not second_number.isalpha() and 
operator in special_character and len(operator) == 1):
    if(second_number == "0" and operator == "/"):
        print("You cannot divide by zero!")
    else:
        if(operator == "+"):
            print(f"{first_number} + {second_number}: {float(first_number) + float(second_number)}")
        elif(operator == "-"):
            print(f"{first_number} - {second_number}: {float(first_number) - float(second_number)}")
        elif(operator == "*"):
            print(f"{first_number} * {second_number}: {float(first_number) * float(second_number)}")
        else:
            print(f"{first_number} / {second_number}: {float(first_number) / float(second_number)}")
else:
    print("Invalid input!")

