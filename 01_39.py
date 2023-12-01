matrix= [[1, 2], 
         [3, 4], 
         [5, 6]]
transpose= map(list, zip(*matrix))
for i in transpose:
    print(i)