li = []
a=0
b=0
for _ in range(9):
    li.append(int(input()))
dif = sum(li) - 100
li.sort()
for i in range(9):
 for j in range(i + 1, 9):
  if li[i] + li[j] == dif:
   a = i
   b = j
for i in range(len(li)):
    if i != a and i != b:
        print(li[i])

# IDE 도움없이 코드작성 연습