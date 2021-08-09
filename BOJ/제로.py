stack = []

K = int(input())

for _ in range(K):
    money = int(input())
    if money != 0:
        stack.append(money)
    else:
        stack.pop()

print(sum(stack))