punctuations="""'"!@#$%^&*()_+-=/;:.,[{]}"""
string= 'This morning, I was walking my dog!'
no_punc= ''
for i in (string):
    if i in punctuations:
        continue
    no_punc+=i
print(no_punc)