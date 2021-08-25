import sys
n = int(input())
a = []
for i in range(n):
    a.append(sys.stdin.readline().rstrip().split())
res = sorted(a, key=lambda x: int(x[0]))
for i in range(len(a)):
    print(res[i][0], res[i][1])

# lambda 공부, split()을 사용해 리스트 안에 리스트 입력받기