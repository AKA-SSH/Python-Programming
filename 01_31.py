def sum_n_cube(x):
    s= 0
    for i in range(1, x+1):
        s+= i
    return s**3
# sample
print(sum_n_cube(3))