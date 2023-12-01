disarium= []
for n in range(1, 101):
    n=  str(n)
    l= len(n)
    s= 0
    for i in range(1, l+1):
        s+= int(n[i-1])**i
    if int(n) == s:
        disarium.append(s)
print(disarium)