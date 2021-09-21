def solution(s):
    if len(s)==1:
        return 1
    res = []
    for split_cnt in range(1, len(s)):
        answer = []
        start = 0
        finish = split_cnt
        splited_word = []
        while True:
            splited_word.append(s[start:finish])
            start = finish
            finish = start + split_cnt
            if finish>len(s):
                splited_word.append(s[start:])
                break
        cnt = 1
        for i in range(1, len(splited_word)):
            if splited_word[i - 1] == splited_word[i]:
                cnt += 1
            else:
                if cnt>1:
                    answer.append(str(cnt))
                answer.append(splited_word[i - 1])
                cnt = 1
        if cnt>1:
            answer.append(str(cnt))
        answer.append(splited_word[-1])
        res.append(len(''.join(answer)))
    return min(res)

# 문자열 처리시 10 과 1 의 구분