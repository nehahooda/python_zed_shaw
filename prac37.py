def cs(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]

print(cs('abcde'))
print(cs('12345'))