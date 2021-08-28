def solution(participant, completion):
    answer = ""
    dict = {}
    for name in participant:
        if name in dict.keys():
            dict[name] += 1
        else:
            dict[name] = 1

    for name in completion:
        if name in dict.keys():
            dict[name] -= 1

    for name in dict.keys():
        if dict.get(name) > 0:
            answer = name
    return answer

# 딕셔너리 자료형을 이용한 해쉬테이블 구현