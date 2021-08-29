n = int(input())
a=[0]*n
a = list(map(int, input().split()))

m = int(input())
b=[0]*m
b = list(map(int, input().split()))

card = {}
for i in range(n):
    card[a[i]]=0
for i in range(n):
        card[a[i]] += 1

for i in range(m):
    if card.get(b[i]):
        print(card[b[i]], end=' ')
    else:
        print("0", end=' ')