import random

sides = 20

c = 0
n = 0

for i in range(1000000):

    a = random.randint(1, sides)
    b = random.randint(1, sides)

    if a > b:
        n = n + a
    else:
        n = n + b
    
    c = c + 1
    if c > 10000:
        print(n)
        c = 0

f = n / 1000000
print(f)