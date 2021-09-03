def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] ==0:
            progresses[i] = (100-progresses[i])//speeds[i]
        else:
            progresses[i] = (100-progresses[i])//speeds[i] + 1
    cnt = 0
    day = progresses[0]
    while progresses:
        if progresses[0] <= day:
            progresses.pop(0)
            cnt += 1
        else:
            day = progresses[0]
            answer.append(cnt)
            cnt = 0
    answer.append(cnt)
    return answer

# 큐, 구현