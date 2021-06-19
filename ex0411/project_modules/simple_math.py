speak_multiplier = 10

def my_calculator(first_number,second_number,operator):
    try:
        if(operator == "+"):
            return float(first_number) + float(second_number)
        elif(operator == "-"):
            return float(first_number) - float(second_number)
        elif(operator == "*"):
            return float(first_number) * float(second_number)
        elif(operator == "/"):
            return float(first_number) / float(second_number)
        else:
            print(f"{operator} is not a valid operator!")

    except Exception as e:
        print(f"Error code: {e}")