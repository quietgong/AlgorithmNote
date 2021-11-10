stk1 = list(input())
stk2 = []
t = int(input())
for _ in range(t):
    c = input()
    if c[0] == "P":
        stk1.append(c[2])
    elif c[0] == "B":
        if stk1:
            stk1.pop()
    elif c[0] == "L":
        if stk1:
            stk2.append(stk1.pop())
    elif c[0] == "D":
        if stk2:
            stk1.append(stk2.pop())

print(''.join(stk1) + ''.join(reversed(stk2)))


# 두 개의 스택을 활용하여 시간복잡도 줄이기