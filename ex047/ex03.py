first_number = input("Input first number: ")
second_number = input("Input second number: ")
operator = input("Input type of operator (+,-,*,/): ")



def my_calculator(first_number,second_number,operator):
    if(operator == "+"):
        return float(first_number) + float(second_number)
    elif(operator == "-"):
        return float(first_number) - float(second_number)
    elif(operator == "*"):
        return float(first_number) * float(second_number)
    else:
        return float(first_number) / float(second_number)

print(my_calculator(first_number,second_number,operator))