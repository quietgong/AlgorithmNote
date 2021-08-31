n = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))
length = sum(distance)
res=0
minimum = city[0]
for i in range(len(city)-1):
    if city[i] < minimum:
        minimum = city[i]
    res += distance[i] * minimum
    length-=distance[i]
print(res)

# 그리디, 아이디어