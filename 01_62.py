w_s= 122122212
b_s= 110010001
b_s_0= 0000000000
def binary_string_check(string):
    string= str(string)
    s= set(string)
    if len(s) == 2 and ('0' in s and '1' in s) or (len(s) == 1 and ('0' in s or '1' in s)):
        return True
    return False
print(binary_string_check(w_s))
print(binary_string_check(b_s))
print(binary_string_check(b_s_0))