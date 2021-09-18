def solution(dartResult):
    li = []
    for i in range(len(dartResult)):
        if dartResult[i] == '0' and dartResult[i - 1] == '1':  # 숫자가 10의 0 일때
            continue
        elif dartResult[i].isdigit():
            li.append(int(dartResult[i]))
            if dartResult[i + 1].isdigit():
                li[-1] = 10
        elif dartResult[i] == "S":
            continue
        elif dartResult[i] == "D":
            li[-1] = li[-1] ** 2
        elif dartResult[i] == "T":
            li[-1] = li[-1] ** 3
        elif dartResult[i] == "*":
            li[-1] *= 2
            if len(li) >= 2:
                li[-2] *= 2
        elif dartResult[i] == "#":
            li[-1] *= -1
    return sum(li)

# 문제이해가 먼저