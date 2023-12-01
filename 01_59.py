k= int(input('enter threshold length:'))
l= ['ant', 'dog', 'rooster', 'dinosaur', 'dragon', 'lion']
n= []
for i in l:
    if len(i) > k:
        n.append(i)
print(n)