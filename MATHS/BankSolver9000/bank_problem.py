import sys
import time
import os

rang = 0
win = 0
valA = []
valB = []
valC = []
max = 0
posc = 0
os.system('cls')

while True:
    del valA
    del valB
    del valC


    rang = 0
    win = 0
    valA = []
    valB = []
    valC = []
    max = 0
    posc = 0








    print("Win amount?   press enter for 1 million")
    while True:
        try:
            win = input()
            win = int(win)
            if win > 0:
                break
            else:
                print("no negitive :<")
        except ValueError:
            if len(win) == 0:
                win = 1000000
                break
            else:
                print("not a number")
                win = 0

    print("Max value for day one and two?   press enter for 1000")
    while True:
        try:
            rang = input()
            rang = int(rang)
            break
        except ValueError:
            if len(rang) == 0:
                rang = 1000
                break
            else:
                print("not a number")
                rang = 0

    while rang > win:
        print("don't do that :<, has to be smaller than Win amount")
        while True:
            try:
                rang = input()
                rang = int(rang)
                break
            except ValueError:
                if len(rang) == 0:
                    rang = 1000
                    break
                else:
                    print("not a number")
                    rang = 0

    print()
    start = time.time()

    for a in range(0, rang):
        per = a / rang * 100
        if per != 0:
            left = round(((time.time() - start)/per)*(100-per)/60, 2)
        else:
            left = 0

        per = format(round(per, 2), '.2f')
        left = format(left, '.2f')

        print(f'  {per}%   {left} mins left', end='\r')

        for b in range(-rang, rang):
            if a == 0 and b == 0:
                continue
            if (a + b) < 0:
                continue
            v1 = a + b
            v2 = v1 + a
            v1 = v2 + v1
            count = 4
            while v1 < win and v2 < win and v1 > -10000 and v2 > -10000:
                v2 = v2 + v1
                count = count + 1
                if v2 == win:
                    valA.append(a)
                    valB.append(b)
                    valC.append(count)
                    print("win!", a, b, "in", count, "days", "            ")

                v1 = v1 + v2
                count = count + 1
                if v1 == win:
                    valA.append(a)
                    valB.append(b)
                    valC.append(count)
                    print("win!", a, b, "in", count, "days", "            ")
    print('                                     ')
    print('\n')
    print('\n')
    print('\n')

    if len(valC) == 0:
        print("No solution found :(")
        sys.exit()

    for i in valC:
        if i > max and valB[posc] >= 0:
            max = i
            pos = posc
        posc = posc + 1

    print('longest =', valA[pos], 'and', valB[pos], 'at', max, 'days')

    posc = 0
    for i in valC:
        if i > max:
            max = i
            pos = posc
        posc = posc + 1


    print('longest sneaky =', valA[pos], 'and', valB[pos], 'at', max, 'days')

    print("solved in", round((time.time() - start)/60, 2), "mins")
    print()
    input("press enter to reset")
    os.system('cls')