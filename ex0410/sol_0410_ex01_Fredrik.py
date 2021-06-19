import sys
from typing import Type, TypeVar

dictionary = dict()

#Welcome / Instructions
print("""Hello and welcome to this dictionary program!
You can at anytime press CTRL+C to end the program.
Use the command line to enter a valid key-value combination("key";"value")
Type "Revert" to revert the dictionary or "Print" to print the existing dictionary
Use "Save" and "Load to save/load to file.""")

while True:
    try:
        user_input = input("Input: ").strip()           
        if len(user_input.split(";")) == 2:              
            user_input = user_input.split(";")                      
            if user_input[0] not in dictionary:         #If key not in dictionary, create new key and [value]
                dictionary[user_input[0]] = [user_input[1]]
            else:                                       #If key already exist, append value
                dictionary[user_input[0]].append(user_input[1])
                
        elif user_input.capitalize() == "Print":        
            print(f"Dictionary: {dictionary}")

        elif user_input.capitalize() == "Count":        
            print(len(dictionary))
            
            

        elif user_input.capitalize() == "Revert":        
            print(f"Dictionary: {dictionary}")
            rev_dictionary = dict()
            for key,value in dictionary.items():
                if str(value) not in rev_dictionary:         #If key not in dictionary, create new key and [value]
                    rev_dictionary[str(value)] = [key]
                else:                                       #If key already exist, append value
                    rev_dictionary[str(value)].append(key)
                
            print(f"Reversed dictionary: {rev_dictionary}")
        
        elif user_input.capitalize() == "Save":
            my_file = open("saved_dict.txt","w")
            data = str(dictionary)
            my_file.write(data)
            my_file.close()
            print("Dictionary has been successfully saved to file.")

        elif user_input.capitalize() == "Load":
            my_file = open("saved_dict.txt","r")
            dictionary = eval(my_file.read())
            my_file.close()
            print("Dictionary has been successfully loaded from file.")

        else:                                           #If input not valid key-value combination
            print("Not a valid key-value combination, try again...")
        
        
    except KeyboardInterrupt:                           
        print("\nThank you for using this program! We hope to see you soon again!")
        sys.exit()