from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        cnt=0
        for i in prices:
            if c>i:
                cnt+=1
                break
            cnt+=1
        answer.append(cnt)
    return answer

# deque를 사용, 맨 앞의 원소부터 비교한 뒤 앞에서부터 pop