def move_disk(num, start, end):
    print(start, end)


def hanoi(num, start, other, end):
    if num==1:
        move_disk(1, start, end)
    else:
        hanoi(num - 1, start, end, other)
        move_disk(num, start, end)
        hanoi(num - 1, other, start, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)