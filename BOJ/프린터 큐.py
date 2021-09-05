t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    li = [[] for _ in range(len(a))]
    for i in range(len(a)):
        li[i].append(a[i])
        li[i].append(i)
    a.sort(reverse=True)
    ans = 0
    while a:
        if li[0][0] >= a[0]:
            if li[0][1] == m:
                ans += 1
                break
            li.pop(0)
            a.pop(0)
            ans += 1
        else:
            x, y = li.pop(0)
            li.append([x, y])
    print(ans)
# 큐와 이차원 배열 활용
