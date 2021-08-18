d = [0]*502
d[0] = 1
d[1] = 1
cnt=0
for i in range(2,len(d)):
    d[i] = d[i-1]*i
n = int(input())
if n==0 or n==1:
    print("0")
else:
    res = list(str(d[n]))
    res.reverse()
    for i in range(len(res)):
        if res[i]=="0":
            cnt+=1
        else:
            break
    print(cnt)

# 포인트 : 0! = 1이다, 파이썬에서 데이터 타입(str, 수, list)간의 변환