special_chars= '!@#$%^&*+-_'
s= 'a%ws we are!'
for i in s:
    if i in special_chars:
        print('has special characters.')
        break