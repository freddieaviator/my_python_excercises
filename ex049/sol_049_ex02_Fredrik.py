import sys

dictionary = dict()

#Welcome / Instructions
print("""Hello and welcome to this dictionary program!
You can at anytime press CTRL+C to end the program.
Use the command line to enter a valid key-value combination("key";"value")
Type "Revert" to revert the dictionary.""")

while True:
    try:
        user_input = input("Input: ").strip()           
        if len(user_input.split(";")) == 2:              
            user_input = user_input.split(";")                      
            if user_input[0] not in dictionary:         #If key not in dictionary, create new key and [value]
                dictionary[user_input[0]] = [user_input[1]]
            else:                                       #If key already exist, append value
                dictionary[user_input[0]].append(user_input[1])
                
            
        elif user_input.capitalize() == "Revert":        
            print(f"Dictionary: {dictionary}")
            rev_dictionary = dict()
            for key,value in dictionary.items():
                if str(value) not in rev_dictionary:         #If key not in dictionary, create new key and [value]
                    rev_dictionary[str(value)] = [key]
                else:                                       #If key already exist, append value
                    rev_dictionary[str(value)].append(key)
                
            print(f"Reversed dictionary: {rev_dictionary}")

        else:                                           #If input not valid key-value combination
            print("Not a valid key-value combination, try again...")
        
        
    except KeyboardInterrupt:                           
        print("\nThank you for using this program! We hope to see you soon again!")
        print(f"""Dictionary: {dictionary}
        Reversed dictionary: {rev_dictionary}""")
        sys.exit()