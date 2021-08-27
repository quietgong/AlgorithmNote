def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [[0]*2 for _ in range(3)]
    score[0][0]=1
    score[1][0]=2
    score[2][0]=3

    for i in range(len(answers)):
        if num1[i%len(num1)] == answers[i]:
            score[0][1]+=1
        if num2[i%len(num2)] == answers[i]:
            score[1][1]+=1
        if num3[i%len(num3)] == answers[i]:
            score[2][1]+=1
    score.sort(key=lambda x:x[1])
    biggest = max(score[0][1], score[1][1], score[2][1])
    for i in range(len(score)):
        if score[i][1] == biggest:
            answer.append(score[i][0])
    return answer