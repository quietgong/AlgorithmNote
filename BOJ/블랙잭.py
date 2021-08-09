import itertools

n, m = map(int, input().split())
arr = [0]*n
arr = list(map(int, input().split()))

combinations = list(itertools.combinations(arr,3)) # arr에서 3개의 정수를 뽑는 경우
sum_list = [0] * len(combinations)

for i in range(len(sum_list)):
    sum_list[i] = sum(combinations[i])

sum_list.sort(reverse=True)

for i in range(len(sum_list)):
    if sum_list[i] <= m:
        ans = sum_list[i]
        break

print(ans)