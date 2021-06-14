current_number = 50
total_numb = 100
bar_length = 10


if(current_number > 0 and current_number < total_numb):
    print(f"""|{"="*(round(((current_number/total_numb)*bar_length))-1)}>{" "*round(((1-current_number/total_numb)*bar_length))}|""")
elif current_number == 0:
    print(f"""|{" " * bar_length}|""")
else:
    print(f"""|{"=" * bar_length}|""") 