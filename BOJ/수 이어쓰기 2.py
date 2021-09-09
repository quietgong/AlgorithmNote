def digit(n):
    count = 0
    length_n = len(str(n))
    for i in range(length_n - 1):
        count += 9 * 10 ** i * (i + 1)
    count = count + (n - 10 ** (length_n - 1) + 1) * length_n
    return count

n,k=map(int, input().split())
length_n = digit(n)
if length_n < k:
    print("-1")
    exit()
cnt=0
i=0
while cnt < k:
    cnt += 9 * 10 ** i * (i + 1)
    i+=1
number = str(10**i + ((k-cnt-1)//i))
print(number[(k-cnt-1)%i])

# 숫자 규칙성