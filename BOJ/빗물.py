h, w = map(int, input().split())
arr = list(map(int, input().split()))
max_h = max(arr)
max_idx = 0
for i in range(len(arr)):
    if arr[i] == max_h:
        max_idx = i
        break
height = arr[0]
total = 0
for i in range(max_idx):
    if height < arr[i + 1]:
        height = arr[i + 1]
    total += height - arr[i + 1]
height = arr[-1]
for i in range(len(arr) - 1, max_idx, -1):
    if height < arr[i - 1]:
        height = arr[i - 1]
    total += height - arr[i - 1]
print(total)

# 가장 큰 값의 인덱스를 기준으로 좌, 우 나눠서 구현(창고 다각형과 유사)