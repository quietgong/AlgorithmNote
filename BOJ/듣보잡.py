# set 자료형의 교집합을 사용해 해결
import sys
n, m = map(int, input().split())
a = [0]*n
b= [0]*m
for i in range(n):
    a[i] = sys.stdin.readline().rstrip()
for i in range(m):
    b[i] = sys.stdin.readline().rstrip()

c = set(a) & set(b)
c = list(c)
c.sort()
print(len(c))
for i in range(len(c)):
    print(c[i])

# dict 자료형을 사용해 해결
import sys
n, m = map(int, input().split())
no_hear = {}
no_see = [0]*m
names = [0] * n
res=[]
for i in range(n):
    names[i] = sys.stdin.readline().rstrip()
for i in range(m):
    no_see[i] = sys.stdin.readline().rstrip()

for i in range(len(names)):
    no_hear[names[i]] = 0

for i in range(len(no_see)):
    if no_see[i] in no_hear:
        res.append(no_see[i])
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])