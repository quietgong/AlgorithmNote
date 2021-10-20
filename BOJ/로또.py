import sys
from itertools import combinations
input=sys.stdin.readline
while True:
    lst=list(map(int, input().split()))
    if len(lst)==1:
        break
    lst=lst[1:]

    for x in combinations(lst, 6):
        print(str(list(x)).replace("[","").replace("]","").replace(",",""))
    print("")

# 조합, 리스트->문자열