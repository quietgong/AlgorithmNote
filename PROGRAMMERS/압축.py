def solution(msg):
    answer = []
    dict={}
    for i in range(26):
        dict[chr(i+65)]=i+1
    w,c=0,0
    while True:
        c+=1
        if c==len(msg):
            answer.append(dict[msg[w:c]])
            break
        if msg[w:c+1] not in dict:
            dict[msg[w:c+1]] = len(dict) + 1
            answer.append(dict[msg[w:c]])
            w=c
    return answer

# dict 자료형, 리스트 슬라이싱 활용 