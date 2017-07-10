#program to reverse a string

def rv1(x):
    y =x.split()
    return" ".join(reversed(y))

def rv2(x):
    y=x.split()
    y.reverse()
    return " ".join(y)

test= raw_input("> Enter a string:")
print rv1(test)
print rv2(test)