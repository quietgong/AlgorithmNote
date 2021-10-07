n = int(input())

a, b, c = map(int, input().split())
max_arr = [a, b, c]
min_arr = [a, b, c]

for i in range(n - 1):
    a, b, c = map(int, input().split())

    temp = list(max_arr)
    max_arr[0] = max(temp[0], temp[1]) + a
    max_arr[1] = max(temp) + b
    max_arr[2] = max(temp[1], temp[2]) + c

    temp = list(min_arr)
    min_arr[0] = min(temp[0], temp[1]) + a
    min_arr[1] = min(temp) + b
    min_arr[2] = min(temp[1], temp[2]) + c

print(max(max_arr), min(min_arr))

# 배열을 복사할때 "="을 사용하면 안된다. 위에서 temp = max_arr이라고 할 경우 temp의 값이 계속 변함.