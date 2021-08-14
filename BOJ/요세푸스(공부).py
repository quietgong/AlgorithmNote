n, m = map(int, input().split())
q = []
ans = []
index = m-1
for i in range(n):
    q.append(i + 1)

for i in range(n):
 if index >= len(q):
  index = index % len(q) # 3명 중 5번째 사람의 위치를 구하는 경우 5%3과 같은 값을 가진다.
  ans.append(q.pop(index)) # pop은 값을 리턴을 먼저하고 삭제
  index += m - 1
 else:
  ans.append(q.pop(index))
  index += m - 1

print("<", ', '.join(str(i) for i in ans), ">", sep="") # join 함수 공부