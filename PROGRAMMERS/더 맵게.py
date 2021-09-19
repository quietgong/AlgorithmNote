import heapq


def solution(scoville, K):
    new_scoville = 0
    heapq.heapify(scoville)
    ans = 0
    while scoville[0] < K:
        new_scoville += heapq.heappop(scoville)
        if len(scoville)==0:
            return -1
        new_scoville += (heapq.heappop(scoville)) * 2
        heapq.heappush(scoville, new_scoville)
        new_scoville = 0
        ans += 1
    return ans

# heapq 문법 숙지, heapify