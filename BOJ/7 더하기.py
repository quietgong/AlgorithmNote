import sys
segment = [[0, 1, 2, 3, 4, 5], [1, 3], [0, 2, 3, 4, 6], [0, 1, 2, 3, 6], [1, 3, 5, 6], [0, 1, 2, 5, 6], [0, 1, 2, 4, 5, 6],
           [0, 1, 3], [0, 1, 2, 3, 4, 5, 6], [0, 1, 3, 5, 6]]
code = ["063", "010", "093", "079", "106", "103", "119", "011", "127", "107"]

def find_sep(data):
    sep = 0
    for i in range(len(data)):
        if data[i] == "+":
            sep = i // 3
            break
    return sep

while True:
    data = sys.stdin.readline().rstrip()    # rstrip()을 해주지 않으면 \n까지 data에 들어감
    if data == "BYE":
        break
    print(data, end='')

    find_sep(data)

    data = data.replace("+", "").replace("=", "")
    arr = []
    for i in range(len(data)):
        if i % 3 == 0:
            arr.append(data[i:i + 3])

    ans = []
    for i in range(len(arr)):
        repeat = 0
        check = []
        a = str(arr[i])
        a_bin = (bin(int(a)).replace("0b", ""))

        while len(a_bin) < 7:
            a_bin = '0' + a_bin

        on = a_bin.count('1')

        for i in range(len(a_bin)):
            if a_bin[i] == "1":
                check.append(6 - i)
            if on == repeat:
                break
        ans.append(check)

    num = []
    for i in range(len(ans)):
        for j in range(len(segment)):
            if sorted(ans[i]) == segment[j]:
                num.append(j)

    a = ''.join(str(_) for _ in num[:sep])
    b = ''.join(str(_) for _ in num[sep:])
    c = int(a) + int(b)
    c = list(str(c))
    res=[]
    for i in c:
        res.append(code[int(i)])
    print(''.join(res))

# 포인트 : 배열<->문자열, join함수