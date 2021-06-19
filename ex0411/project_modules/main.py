from graphic.print_text import say_my_name
from graphic.print_text import say_many_names
from simple_math import my_calculator
from simple_math import speak_multiplier

def main():
    say_many_names(speak_multiplier)

    while True:
        first_number = input("Input first number: ")
        second_number = input("Input second number: ")
        operator = input("Input type of operator (+,-,*,/): ")
        print(my_calculator(first_number,second_number,operator))
        choice = input("Would you like to calculate more? (y/n): ")
        if(choice.lower() == "y"):
            continue
        else:
            break



if __name__=='__main__':
    main()