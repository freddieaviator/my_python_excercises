punishment_text = "I will not teach others to fly that good"
numb_of_repetition = 10

punishment_text = punishment_text.replace("not","")
punishment_text = punishment_text.replace("good","bad")

print((punishment_text + "\n") * numb_of_repetition )
print(f"""The occurrence of the word THAT in the original sentence is: {punishment_text.count("that")}""")