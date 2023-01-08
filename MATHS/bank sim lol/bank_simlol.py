import os
import math

def get_num_digits(n: int) -> int:
    if n < 0:
        return get_num_digits(-n)
    elif n < 10:
        return 1
    else:
        return math.floor(math.log10(n)) + 1


a = 0
b = 0
os.system('cls')

while True:
    day = 1

    a = int(input("deposit day 1 = "))
    b = int(input("deposit day 2 = "))

    print()

    print("day", day, "=", format(a, ','))
    v1 = a + b
    day = day + 1
    print("day", day, "=", format(v1, ','))
    v2 = v1 + a
    day = day + 1
    print("day", day, "=", format(v2, ','))

    while v1 < 1000000 and v2 < 1000000:
        v1 = v2 + v1
        day = day + 1
        print("day:", day, "digits:", get_num_digits(v1), end='\r')
        if v1 >= 1000000:
            break
        v2 = v1 + v2
        day = day + 1
        print("day:", day, "digits:", get_num_digits(v2), end='\r')
    print()
    input("press enter")
    os.system('cls')