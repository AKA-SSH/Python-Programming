array= [1, 2, 3, 4, 5, 6, 7, 8, 9]
l= len(array)
m= l//2 if l%2==0 else (l+1)//2
a1, a2= array[:m], array[m:]
new_array= a2+a1
print(new_array)