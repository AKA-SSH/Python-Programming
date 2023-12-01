l= [1, 2, 'aaa', None, 5, None]
remove_empty= []
for i in l:
    if i == None:
        continue
    else:
        remove_empty.append(i)
print(remove_empty)