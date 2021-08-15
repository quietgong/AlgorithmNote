n = str(input())
a = []
for i in range(len(n)):
    a.append(n[i])
a.sort(reverse=True)
for i in range(len(n)):
    print(a[i], end='')