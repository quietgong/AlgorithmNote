t = int(input())
for _ in range(t):
    n = int(input())
    if n ==0:
        print("0")
        continue
    arr = []
    freq = []
    for i in range(n):
        name,category = map(str, input().split())
        arr.append(category)

    arr2 = list(set(arr))
    for i in range(len(list(set(arr2)))):
        freq.append(arr.count(arr2[i]))
    res=1
    for i in range(len(freq)):
        res*=freq[i]+1
    res-=1
    print(res)

# 포인트 : 각 옷 종류에 입지 않는 경우도 생각하여 곱해준다.
# 예) headgear : 2, eyewear : 1 -> headgear : 1번, 2번, 안입는경우, eyewear : 1번, 안입는경우
# 2*1 - 1(안입는경우, 안입는경우)