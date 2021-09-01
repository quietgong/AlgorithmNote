MAX = 1000001
d = [0] * MAX
d[1] = 1
d[2] = 2
for i in range(3, MAX):
    d[i] = (d[i - 1] + d[i - 2]) % 15746

n = int(input())
print(d[n])

# 해설 : https://sungmin-joo.tistory.com/21
