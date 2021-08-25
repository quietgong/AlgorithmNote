import sys

n = int(input())
word = [0] * n
arr = []
res = []
for i in range(n):
    word[i] = sys.stdin.readline().rstrip()
for i in range(len(word)):
    if word[i] not in arr:
        arr.append(word[i])
arr = sorted(arr)
for i in range(1, 51):
    for j in range(len(arr)):
        if len(arr[j]) == i:
            res.append(arr[j])

for i in range(len(res)):
    print(res[i])

# 문자열을 sort하면 각 원소의 맨 앞글자 사전 순으로 정렬된다.