s= 'hellooooo... kya karre hoooo...'
n= ''
i= int(input('enter the character index:'))
if 0 > i > len(s):
    print('out of bound')
    exit()
for index, value in enumerate(s):
    if index == i:
        continue
    else:
        n+=value
print(n)