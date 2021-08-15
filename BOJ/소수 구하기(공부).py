n,m = map(int, input().split())
arr = [0]*(m+1)
arr[0] = False
arr[1] = False

for i in range(2, m+1):
    arr[i] = True

for i in range(2, m):
    if arr[i]:
        for j in range(i*2, m+1, i): # j는 i*2값부터 시작하여 m+1까지 i만큼의 값으로 증가하면서 반복문을 진행
            arr[j] = False

for i in range(len(arr)):
    if arr[i] and i>=n:
        print(i)

# 포인트 : 배열에 True 와 False를 넣어 인덱스를 소수 자체로 해결