from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    ans=0
    while people:
        if len(people)==1:
            ans+=1
            break
        if people[0]+people[-1]>limit:
            people.popleft()
        else:
            people.popleft()
            people.pop()
        ans+=1
    return ans

# 아이디어
# 가장 몸무게가 많이 나가는 사람과 가장 몸무게가 적게 나가는 사람을 더해서 제한보다 작으면
# 맨 앞과 맨 뒤를 pop
# 그렇지 않으면 가장 몸무게가 많이 나가는 사람만 pop