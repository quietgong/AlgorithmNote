n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
for i in range(n):
    for j in range(i + 1):
        res += arr[j]
print(res)

# 그리디 (정렬을 통해 제일 적은수부터 덧셈이 되도록)