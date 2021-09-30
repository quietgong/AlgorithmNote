n=int(input())
a=[]
max_height=0

for _ in range(n):
    x,h=map(int, input().split())
    max_height=max(max_height,h)
    a.append([x,h])
a.sort(key=lambda x:x[0])
idx=0

for i in range(len(a)):
    if a[i][1]==max_height:
        idx=i
        break
for i in range(idx):
    if a[i][1] >= a[i+1][1]:
        a[i+1][1]=a[i][1]
for i in range(len(a)-1, idx, -1):
    if a[i][1] >= a[i-1][1]:
        a[i-1][1]=a[i][1]
total=0
for i in range(idx):
    total+=(a[i+1][0]-a[i][0])*a[i][1]
for i in range(len(a)-1, idx, -1):
    total+=(a[i][0]-a[i-1][0])*a[i][1]
print(total+max_height)

# 가장 큰 값의 인덱스를 기준으로 좌, 우 나눠서 구현(창고 다각형과 유사)