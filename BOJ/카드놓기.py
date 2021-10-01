from itertools import permutations

n=int(input())
k=int(input())
card=[]
x=[]
for _ in range(n):
    card.append(int(input()))

for i in permutations(card,k):
    i=list(i)
    for j in range(len(i)):
        i[j]=str(i[j])
    x.append(''.join(i))

print(len(set(x)))

# 순열, 조합 공부