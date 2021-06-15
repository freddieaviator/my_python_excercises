students = ["Fredrik Hårberg","Susan Klingsell","Alexis Kan","Tonje Andersen","Rasmus Andreasson"]

print(students[2])

print(students[2][0])

students[2] = "Ole"

students[2] += " Nordmann"

students += ["Alexis Kan"]

students.insert(4,"Monty Python")

print(len(students))

students.remove("Ole Nordmann")

print(len(students))

print(students.index("Monty Python"))

print(students[:3])

students_reverse = students[::-1]

students_even = students[::2]

students_odd = students[1::2]


print(students)
print(students_reverse)
print(students_even)
print(students_odd)