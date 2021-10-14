def solution(str1, str2):
    str1, str2=str1.upper(), str2.upper()
    s1,s2,common=[],[],[]
    
    for i in range(len(str1)-1):
        if 'A'<=str1[i]<='Z' and 'A'<=str1[i+1]<='Z':
            s1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if 'A'<=str2[i]<='Z' and 'A'<=str2[i+1]<='Z':
            s2.append(str2[i:i+2])
    
    if len(s1)>len(s2):
        s1,s2=s2,s1
    union = s1 + s2
    for i in s1:
        if i in s2:
            common.append(i)
            s2.remove(i) # s1에서 더해줬으면 s2에서 삭제해줘야 한다.
    for i in common:
        union.remove(i)
    if len(union)==0:
        return 65536
    return int((len(common)/len(union))*65536)

# 교집합을 구할때의 예외처리