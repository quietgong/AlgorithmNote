from bisect import bisect_left, bisect_right


def calCountsByRange(arr, value):
    r_i = bisect_right(arr, value)
    l_i = bisect_left(arr, value)
    if r_i - l_i > 0:
        print("1")
    else:
        print("0")


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
find = list(map(int, input().split()))
for i in range(m):
    calCountsByRange(arr, find[i])

# 포인트 : 이분탐색 (정렬된 리스트로)