import sys
count = [0] * 10000
n = int(input())
for i in range(n):
    count[int(sys.stdin.readline()) - 1] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i + 1)
# 포인트 : 카운트 정렬, 이중 for문을 활용해 인덱스에 해당하는 값만큼 출력하기
