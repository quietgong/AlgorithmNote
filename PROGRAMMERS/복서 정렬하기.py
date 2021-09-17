def solution(weights, head2head):
    info = []
    for i in range(len(head2head)):
        overWin = 0
        win = 0
        stage = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                stage += 1
                if head2head[i][j] == 'W':
                    win += 1
                    if weights[i] < weights[j]:
                        overWin += 1
        if stage != 0:
            winper = win / stage * 100
        else:
            winper = 0
        info.append([i + 1, weights[i], winper, overWin])

    ans = sorted(info, key=lambda x: (x[2], x[3], x[1], -x[0]), reverse=True)
    return [num[0] for num in ans]

# 람다를 이용한 다중 정렬식