def recursive(x,y,N,arr):
    num=arr[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j]!=num:
                recursive(x,y,N//2,arr)
                recursive(x+N//2,y,N//2,arr)
                recursive(x,y+N//2,N//2,arr)
                recursive(x+N//2,y+N//2,N//2,arr)
                return
    if num==0:
        result.append(0)
    else:
        result.append(1)

result=[]
def solution(arr):
    recursive(0,0,len(arr),arr)
    return [result.count(0),result.count(1)]

# 분할정복