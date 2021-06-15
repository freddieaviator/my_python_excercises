values = [23,54,76,34,97,56,87,45,76,12,3,49,92]
alpha = 0.5

values = sorted(values)

lower_index = round(len(values)*alpha/2)
upper_index = round(len(values)*(1-alpha/2)) -1

print(f"""Lower values: {values[:lower_index]}
Upper values: {values[upper_index:]}""")