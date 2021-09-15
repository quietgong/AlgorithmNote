def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -1

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] - 1 == reserve[j] or lost[i] + 1 == reserve[j]:
                lost[i] = -1
                reserve[j] = -1

    cnt = 0
    for i in range(len(lost)):
        if lost[i] != -1:
            cnt += 1
    return n - cnt

# 그리디 (여벌의 옷을 가져온 학생이 도난당했을 경우, 여벌의 옷을 자신에게 먼저 준다.)