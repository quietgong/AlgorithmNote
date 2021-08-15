n = int(input())
w = [0] * n
h = [0] * n
ans = [0] * n
for i in range(n):
    w[i], h[i] = map(int, input().split())

for i in range(n):
    ranking = 1
    for j in range(n):
        if w[i]>w[j] and h[i] > h[j]:
            continue
        elif w[i]<w[j] and h[i] < h[j]:
            ranking+=1
    ans[i]=ranking

for i in range(len(ans)):
    print(ans[i], end=' ')