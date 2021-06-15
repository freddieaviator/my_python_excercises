captured = "Pikachu","Pidgey","Abra","Pidgey","Eevee","Pidgey"

pokemon = input("Please enter the Pokémon caught: ")

if(pokemon in captured):
    print("Already captured!")
else:
    print("New Pokémon!")

print(f"Total number of Pokémons in tuple: {len(captured)}")

captured_set = set(captured)

print(f"Amount of unique Pokémons: {len(captured_set)}")