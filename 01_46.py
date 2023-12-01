def harshad_number(n):
    s= 0
    str_n= str(n)
    l= len(str_n)
    for i in range(l):
        s+= int(str_n[i])
    if n%s == 0:
        return 'harshad number'
    else:
        return 'some random ass number'
# sample
print(harshad_number(18))
print(harshad_number(15))