def solution(records):
    info={}
    ans=[]
    for record in records:
        record=record.split(' ')
        if len(record)>=3:
            info[record[1]]=record[2]
    for record in records:
        record=record.split(' ')
        if record[0]=="Enter":
            ans.append(info.get(record[1]) + "님이 들어왔습니다.")
        elif record[0]=="Leave":
            ans.append(info.get(record[1]) + "님이 나갔습니다.")

    return ans

# dict 자료형 사용법 숙지