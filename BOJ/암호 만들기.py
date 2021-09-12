from itertools import combinations

n, m = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
arr = list(map(str, input().split()))
arr.sort()
pw_list = []

for x in combinations(arr, n):
    cnt = 0
    for vowel in vowels:
        if vowel in list(x):
            cnt += 1
    if cnt >= 1 and len(list(x)) - cnt >= 2:
        print(''.join(x))

# 풀기 전 문제의 조건과 요구를 꼼꼼히, 정확히 읽는다.