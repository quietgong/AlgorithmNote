import sys


def how_2_times(n):
    cnt = 0
    while n >= 2:
        cnt += n // 2
        n = n // 2
    return cnt


def how_5_times(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n = n // 5
    return cnt


n, m = map(int, sys.stdin.readline().split())
print(min(how_2_times(n) - how_2_times(n - m) - how_2_times(m), how_5_times(n) - how_5_times(n - m) - how_5_times(m)))

# 포인트 : 0의 개수는 2와 5의 짝지을 수 있는 승수의 개수로 결정된다. 예) 2*5^2 = 50 (0의 개수:1)
