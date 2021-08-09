T = int(input())

for _ in range(T):
    string = list(input())
    stack = []

    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        else:
            if '(' in stack: # in을 생각하기 어려웠다.
                stack.pop()
            else:
                stack.append(')')

    if len(stack) == 0 :
        print("YES")
    else:
        print("NO")