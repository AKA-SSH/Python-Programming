import cmath # used for handling complex numbers
a= float(input('Enter x^2 coefficient:'))
b= float(input('Enter x^1 coefficient:'))
c= float(input('Enter x^0 coefficient:'))
discriminant= cmath.sqrt(b**2 - 4*a*c)
print(f'root 1: {(-b + discriminant)/(2*a)}\nroot 2: {(-b - discriminant)/(2*a)}')