def solution(n):
    answer = ''
    num=[4,1,2]
    while n>0:
        n,mod=divmod(n,3)
        if mod==0:
            n-=1
        answer+=str(num[mod])
    return answer[::-1]

# 3번 반복되는 규칙으로 해결