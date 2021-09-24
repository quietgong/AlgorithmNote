n, k = map(int, input().split())
arr=list(map(int, input().split()))
start,end = 0, max(arr)
while start <= end:
    trees = 0
    mid = (start + end) // 2
    for x in arr:
        if (x-mid)>0:
            trees += x - mid
    if trees < k: # 자른 나무가 원하는 개수보다 적으면 더 많이 잘라야됨.
        end = mid-1
    else:
        res=mid # 최대한 나무를 덜 잘랐을 때가 정답이므로
        start = mid+1

print(res)

# 파라메트릭 서치