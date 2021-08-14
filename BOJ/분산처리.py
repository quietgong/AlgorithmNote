T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    if a > 10:
        a = a % 10

    a = a % 10




    if a == 0:
        print("10")
    if a == 1:
        print("1")
    elif a == 2:
        b = b - 1
        if b % 4 == 0:
            print("2")
        elif b % 4 == 1:
            print("4")
        elif b % 4 == 2:
            print("8")
        elif b % 4 == 3:
            print("6")
    elif a == 3:
        b = b - 1
        if b % 4 == 0:
            print("3")
        elif b % 4 == 1:
            print("9")
        elif b % 4 == 2:
            print("7")
        elif b % 4 == 3:
            print("1")
    elif a == 4:
        if b % 2 == 0:
            print("6")
        else:
            print("4")
    elif a == 5:
        print("5")
    elif a == 6:
        print("6")
    elif a == 7:
        b = b - 1
        if b % 4 == 0:
            print("7")
        elif b % 4 == 1:
            print("9")
        elif b % 4 == 2:
            print("3")
        elif b % 4 == 3:
            print("1")
    elif a == 8:
        b = b - 1
        if b % 4 == 0:
            print("8")
        elif b % 4 == 1:
            print("4")
        elif b % 4 == 2:
            print("2")
        elif b % 4 == 3:
            print("6")
    elif a == 9:
        if b % 2 == 0:
            print("1")
        else:
            print("9")