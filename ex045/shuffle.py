import random

students = ["Adam","Bertil","Ceasar","David","Erik","Filip","Gustav","Helge","Ivar","Johan","Kalle"]

random.shuffle(students)

students.insert(0,"Group 1: ")
students.insert(5,"Group 2: ")
students.insert(10,"Group 3: ")

for student in students:
    print(student)




