import sys

def solution(sentence):
    stack = []
    for i in range(len(sentence)):
        if sentence[i] == '[':
            stack.append('[')
        if sentence[i] == ']':
            if '[' not in stack or stack[-1] == "(":
                return False
            else:
                stack.pop()
        if sentence[i] == '(':
            stack.append('(')
        if sentence[i] == ')':
            if '(' not in stack or stack[-1] == "[":
                return False
            else:
                stack.pop()

    if len(stack)==0:
        return True
    else:
        return False

sentences = []
while True:
    n = sys.stdin.readline().rstrip()
    if n == '.':
        break
    sentences.append(n)

ans = []
for i in range(len(sentences)):
    res = solution(sentences[i])
    if res:
        ans.append("yes")
    else:
        ans.append("no")

for i in ans:
    print(i)