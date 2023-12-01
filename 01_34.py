def rotate(array):
    new_array= [array[-1]]
    l= len(array)
    for i in range(l-1):
        new_array.append(array[i])
    return new_array
# sample
array= [1,2,3,4,5]
print(rotate(rotate(array))) # after 2 rotations