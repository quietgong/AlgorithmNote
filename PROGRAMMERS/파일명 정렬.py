def solution(files):
    ans = []
    for file in files:
        origin=file
        head_idx=0
        number_idx=0
        for i in range(len(file)):
            if file[i].isdigit():
                head_idx=i
                break
        file_head = file[:head_idx].lower()
        file = file[head_idx:]
        for i in range(len(file)):
            if not file[i].isdigit():
                number_idx=i
                break
        if number_idx==0:
            file_number=int(file)
        else:
            file_number = int(file[:number_idx])
        file_tail=file[number_idx:]
        ans.append([origin,file_head,file_number,file_tail])

    ans.sort(key=lambda x:(x[1],x[2]))
    res=[]
    for i in range(len(ans)):
        res.append(ans[i][0])

    return res

# 인덱스 활용