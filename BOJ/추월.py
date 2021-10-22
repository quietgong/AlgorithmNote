# 스택을 활용한 풀이
n=int(input())
ans=0
stack=[]
for _ in range(2*n):
    car_num=input()
    if car_num not in stack:
        stack.append(car_num)
    else:
        if stack[0]==car_num:
            stack.pop(0)
        else:
            stack.remove(car_num)
            ans+=1
print(ans)

# 해시를 활용한 풀이
n = int(input())
ans = 0
enter, out = dict(), []
for i in range(n):
    car = input()
    enter[car] = i
for _ in range(n):
    car = input()
    out.append(car)

for i in range(n - 1):
    for j in range(i + 1, n):
        if enter[out[i]] > enter[out[j]]: # 다음 차 확인
            ans += 1
            break
print(ans)