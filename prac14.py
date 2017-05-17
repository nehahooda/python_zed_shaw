import random

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ?.,<>!@#$%^&*()"

paslen =8
p = "".join(random.sample(s,paslen))
print p