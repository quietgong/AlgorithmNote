def solution(new_id):
    new_id = new_id.lower()
    answer=[]
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == '_' or new_id[i] == '.' or new_id[i] == '-':
            answer.append(new_id[i])
        else:
            continue
    answer = ''.join(answer)
    while ".." in answer:
        answer = answer.replace("..", ".")

    answer=list(answer)
    if answer[0] == '.':
        answer.pop(0)
    elif answer[-1] == '.':
        answer.pop()
    if len(answer) == 0:
        answer.append("a")

    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer.pop()
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return ''.join(answer)


# isalpha, isdigit 함수 활용