a= [1, 2, 3, 4, 5, 6]
b= [6, 5, 4, 3, 2, 1]
c= [1, 1, 1, 1, 1, 1]
d= [1, 2, 4, 2, 5, 2]
def check_monotonic(array):
    response= []
    l= len(array)
    for i in range(1, l):
        if array[i]-array[i-1] > 0:
            response.append('increasing')
        elif array[i]-array[i-1] < 0:
            response.append('decreasing')
        else:
            response.append('no change')
    if len(set(response)) == 1:
        return 'monotonic'
    return 'not monotonic'
# sample
print(check_monotonic(a))
print(check_monotonic(b))
print(check_monotonic(c))
print(check_monotonic(d))