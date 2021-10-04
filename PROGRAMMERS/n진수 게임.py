alpha = ['A', 'B', 'C', 'D', 'E', 'F']


def convert(n, q, arr):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += alpha[mod - 10]
        else:
            rev_base += str(mod)
    for i in range(len(rev_base)):
        arr.append(rev_base[::-1][i])


def solution(n, t, m, p):
    answer = ''
    a = ['0']
    for i in range(1, m * t):
        convert(i, n, a)
    for i in range(t):
        answer += (a[p - 1])
        p = p + m
    return answer

# 진수 변환