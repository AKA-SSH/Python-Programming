d= {'key':['a', 'b', 'c'],
    'value':[1, 2, 3]}
flatten= dict(zip(d['key'], d['value']))
print(flatten)