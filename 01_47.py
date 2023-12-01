harshad_numbers= []
for n in range(1, 101):
    s= 0
    str_n= str(n)
    l= len(str_n)
    for i in range(l):
        s+= int(str_n[i])
    if n%s == 0:
        harshad_numbers.append(n)
# result
print(harshad_numbers)