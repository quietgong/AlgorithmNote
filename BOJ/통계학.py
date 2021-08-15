import sys
N = int(sys.stdin.readline())
arr = [0]*N
def mode(arr):
    list = [0]*N
    res = []
    for i in range(N):
        list.append(abs(arr[i]))
    scope = max(list) # arr 원소 중 절댓값으로 가장 큰 값을 scope로 지정한다.
    freq = [0] * ((scope*2)+1) # scope 만큼 초기화
    for i in range(N):
        freq[arr[i] + scope] += 1
    idx = max(freq)
    for i in range(len(freq)):
        if freq[i] == idx:
            res.append(i - scope)
    res.sort()

    if len(res)==1:
        return res[0]
    else:
        return res[1]

for i in range(N):
    arr[i] = int(sys.stdin.readline())

arr.sort()

print(round(sum(arr)/N))
print(arr[N//2])
if N==1:
    print(arr[0])
else:
    print(mode(arr))
print(max(arr)-min(arr))

# 포인트 : 최빈값 구하기가 까다로움, import sys, sys.stdin.readlines()