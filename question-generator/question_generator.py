import random

my_file = open("question.txt", encoding="utf8")
content_list = my_file.readlines()

random.shuffle(content_list)

print(f"""
--------The Question-of-the-day-generator has spoken!-------
============================================================
{content_list[0]}
============================================================""")

