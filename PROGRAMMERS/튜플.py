def solution(s):
    s=s.lstrip('{').rstrip('}').split('},{')
    li=[]
    ans=[]
    for i in s:
        li.append(i.split(','))
    li.sort(key=len)
    for i in range(len(li)):
        for j in range(len(li[i])):
            if int(li[i][j]) not in ans:
                ans.append(int(li[i][j]))
    return ans

# sort(key=len) 배열 원소의 길이대로 정렬한다.
# 정렬 전 : [['1', '2', '3'], ['2', '1'], ['1', '2', '4', '3'], ['2']]
# 정렬 후 : [['2'], ['2', '1'], ['1', '2', '3'], ['1', '2', '4', '3']]