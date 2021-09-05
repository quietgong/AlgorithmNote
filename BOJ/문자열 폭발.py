import sys
s = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
stack = []
for i in range(len(s)):
    stack.append(s[i])
    if stack[-1] == word[-1] and len(stack) >= len(word):
        check = ""
        for i in range(len(word), 0, -1):
            check += stack[-i]
        if check == word:
            for _ in range(len(word)):
                stack.pop()
stack = ''.join(stack)
if len(stack) == 0:
    print("FRULA")
else:
    print(stack)

# 스택 자료구조