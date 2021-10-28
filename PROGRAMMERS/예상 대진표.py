def solution(n, a, b):
    answer = 0
    while a!=b:
        answer+=1
        a=(a//2)+(a%2)
        b=(b//2)+(b%2)

    return answer

# 토너먼트 특성을 활용해 숫자 규칙 찾는 문제
# 어떤 정수 n의 다음 토너먼트 번호는 n//2 와 n%2 를 더한 값이 된다.