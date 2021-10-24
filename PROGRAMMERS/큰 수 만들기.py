def solution(number, k):
    stk = []
    for i in number:
        while stk and stk[-1] < i and k>0: # 스택이 비어있지 않고, 스택의 마지막 값보다 들어오는 값이 크고, k가 0보다 크다면
            k-=1
            stk.pop()
        stk.append(i)
    return "".join(stk[:len(stk)-k]) # 만약 k가 0보다 클때의 경우를 위해