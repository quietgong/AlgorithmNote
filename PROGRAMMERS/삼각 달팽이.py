def solution(n):
    arr=[[0]*n for _ in range(n)]
    x,y=-1,0
    answer=[]
    num=1
    for i in range(n):
        for j in range(i,n):
            if i%3==0: # 밑으로
                x+=1  
            elif i%3==1: # 오른쪽으로
                y+=1
            elif i%3==2: # 위로
                x-=1
                y-=1
            
            arr[x][y]=num
            num+=1
    
    for i in arr:
        for j in i:
            if j!=0:
                answer.append(j)
    return answer

# 리스트 인덱스 다루기