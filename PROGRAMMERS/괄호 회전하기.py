from collections import deque


def is_right(s):
    stack = []
    for i in s:
        if len(stack) != 0:
            if stack[-1] == "(" and i == ")":
                stack.pop()
                continue
            elif stack[-1] == '[' and i == ']':
                stack.pop()
                continue
            elif stack[-1] == '{' and i == '}':
                stack.pop()
                continue
        stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    q = deque(s)
    answer = 0
    for i in range(len(s)):
        if is_right(q):
            answer += 1
        q.rotate(1)
    return answer

# rotate(파라미터)는 deque를 사용