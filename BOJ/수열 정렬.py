n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
p = []
for i in range(n):
    p.append(b.index(a[i]))
    b[b.index(a[i])] = -1
print(*p)

# index 활용, 리스트에 * 연산자를 붙이고 출력하면 각 원소마다 띄어져서 출력된다.