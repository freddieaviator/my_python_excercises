import time

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
course = input("What is the name of your course?: ")
candidates = int(input("How many candidates are in the course?: "))

print("My name is", end= " ")
print(first_name, end= " ") 
print("with last name", end= " ") 
print(last_name, end= " ")
print("I am participating in the course", end= " ") 
print(course, end= ". ") 
print("There are", end= " ") 
print(candidates, end= " ") 
print("candidates taking the", end= " ") 
print(course, end= " ") 
print("course.")