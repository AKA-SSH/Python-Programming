import math
def LCM(a, b):
    return abs(a*b)//math.gcd(a, b)
# sample
s= LCM(10, 15)
print(s)