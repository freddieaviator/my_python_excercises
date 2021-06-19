dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dictionary = dict(dic1)
dictionary.update(dic2)
dictionary.update(dic3)
print(dictionary)

def unfold_dict(dict):
    return {**dict}

input_dict = {
    'a':{'d':1, 'e':2},
    'b':{'f':3},
    'c':{'g':4, 'h':5}
}

new_dict = unfold_dict(input_dict)
print(new_dict)