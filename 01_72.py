d= {'a': 1,
    's': 9,
    'c': 7,
    'e': 10}
print(sorted(d.items(), key= lambda x: x[0])) # sort by keys
print(sorted(d.items(), key= lambda x: x[1])) # sort by values