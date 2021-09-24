def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(l):
        if citations[i] >= n-i:
            return n-i
    return 0

# 인덱스와 원소의 값 비교