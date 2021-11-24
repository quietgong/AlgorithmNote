n=int(input())
arr=list(map(int, input().split()))
arr.sort()
ans=int(input())
cnt=0
s,e=0,n-1
while s<e:
    if arr[s]+arr[e]>ans:
        e-=1
    elif arr[s]+arr[e]<ans:
        s+=1
    else:
        s+=1
        cnt+=1
print(cnt)

# 투 포인터를 정상적으로 사용하기 위해 정렬을 한다.
# ans에 점점 인접하도록 s,e의 값을 조정해준다.