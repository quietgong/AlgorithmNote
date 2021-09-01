n = input()
status = 1
ans = 0
tmp=0
for i in range(len(n)):
    if n[i] != '-' and n[i] != '+':
        tmp = (tmp * 10) + (int(n[i])) * status
    elif n[i] == '+':
        ans += tmp
        tmp = 0
    elif n[i] == '-':
        status = -1
        ans += tmp
        tmp = 0

print(ans+tmp)

# status 상태 변경