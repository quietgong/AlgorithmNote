from collections import deque
from itertools import permutations
def solution(expression):
    ops=['*','+','-']
    li=[]
    priority=[]
    s=0
    answer=0
    for i,v in enumerate(expression):
        if v in ops:
            li.append(expression[s:i])
            li.append(v)
            s=i+1
    else:
        li.append(expression[s:])

    for op in ops:
        if op not in li:
            ops.remove(op)
    priority=permutations(ops)
    
    for case in priority:
        stacks = [deque(li), deque()]
        t1 = 1
        for c in case: # 각 경우에서 연산자 처리
            t1 = (t1+1) % 2 # 스택 토글 변수
            t2 = (t1+1) % 2
            while len(stacks[t1]):
                item = stacks[t1].popleft()
                if len(stacks[t2]) and stacks[t2][-1] == c:
                    c = stacks[t2].pop()
                    n = stacks[t2].pop()
                    item = str(eval(str(n)+c+str(item)))
                stacks[t2].append(item)
            
        result = stacks[len(ops)%2].pop()
        result = abs(int(result))
        answer = max(answer, result)
    return answer

# eval 함수