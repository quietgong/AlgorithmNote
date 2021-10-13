from itertools import combinations
from collections import Counter


def solution(orders, course):
    ans = []
    for i in course:
        candidate = []
        for order in orders:
            candidate += combinations(sorted(order), i)
        counter = Counter(candidate)

        if counter:
            max_ = max(list(counter.values()))
            if max_ >= 2:
                for key, value in counter.items():
                    if counter[key] == max_:
                        ans.append(''.join(key))
    return sorted(ans)


# Counter 모듈 사용법