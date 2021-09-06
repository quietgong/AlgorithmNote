import sys
n=int(input())
res=[]
a=[]
symbol=[]
ans=[]
for i in range(n):
    res.append(int(sys.stdin.readline()))

for i in range(n):
    a.append(i+1)
    symbol.append('+')
    if len(a)>0 and a[-1]==res[0]:
        while a[-1] == res[0]:
            res.pop(0)
            ans.append(a.pop())
            symbol.append('-')
            if len(a)<=0:
                break

if len(a)==0:
    for i in symbol:
        print(i)
else:
    print("NO")
    
# 스택의 구조를 생각하면서 idx[-1]과 pop(0)을 적절히 사용한다.