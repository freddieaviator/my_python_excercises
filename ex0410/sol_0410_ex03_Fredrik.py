import csv

d = {}

try:
    my_file = open("TSLA.csv","r")
    reader = csv.reader(my_file)
    counter = 0
    for row in reader:
        if counter > 0:
            k,v1,v2,v3,v4,v5,v6 = row
            d[k] = [v1,v2,v3,v4,v5,v6]
        counter += 1
    
    for key, value in d.items():
        print(f"{key}:{value}")

except Exception as e:
    print(f"Error code: {e}")
