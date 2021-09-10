a, b = map(int, input().split())
a = list(str(a))
b = list(str(b))

ans = 0
if len(a) != len(b):
    print(ans)
else:  # a와 b의 자리수가 같을때
    for i in range(len(b)):
        if a[i] != b[i]:
            break
        else:
            if a[i] == '8':
                ans += 1
    print(ans)

# 자릿수가 같을때와 다를때의 아이디어