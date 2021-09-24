n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
start,end = 1, max(arr)
while start <= end:
    lines = 0
    mid = (start + end) // 2
    for x in arr:
        lines += x // mid

    if lines >= k:
        start = mid+1
    else:
        end = mid-1
print(end)

# 파라메트릭 서치
# start는 mid+1, end = mid-1 (그렇지 않으면 답이 start or end인 경우 무한루프에 빠진다.)