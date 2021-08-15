num = 666
devil_num = []
n = int(input())
while True:
    if len(devil_num)==n:
        break
    if '666' in str(num):
        devil_num.append(num)
    num+=1

print(devil_num[-1])