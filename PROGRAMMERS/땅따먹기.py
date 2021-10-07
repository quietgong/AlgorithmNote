def solution(land):
    n = len(land)
    a, b, c, d = land[0][0], land[0][1], land[0][2], land[0][3]
    arr = [a, b, c, d]
    for i in range(1, n):
        a, b, c, d = land[i][0], land[i][1], land[i][2], land[i][3]
        temp = list(arr)
        arr[0] = max(temp[1], temp[2], temp[3]) + a
        arr[1] = max(temp[0], temp[2], temp[3]) + b
        arr[2] = max(temp[0], temp[1], temp[3]) + c
        arr[3] = max(temp[1], temp[2], temp[0]) + d
    return max(arr)

# 백준(내려가기) (범위 3)와 유사