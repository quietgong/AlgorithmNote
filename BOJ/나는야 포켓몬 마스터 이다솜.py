import sys
n, m = map(int, input().split())
dic = {}
q=[0]*m
names = [0] * n
for i in range(n):
    names[i] = sys.stdin.readline().rstrip()
for i in range(len(names)):
    dic[names[i]] = str(i+1)
for i in range(m):
    q[i] = input()
for i in range(len(q)):
    if dic.get(q[i]):
        print(dic.get(q[i]))
    else:
        print(names[int(q[i])-1])

# 딕셔너리, 형변환