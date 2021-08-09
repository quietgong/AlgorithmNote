num = int(input())
for i in range(1, num+1):
    coef_num_list = list(map(int, str(i)))

    a = i + sum(coef_num_list) # 입력받은 num과 num의 각 자리 수를 더한 값을 할당

    if a == num:
        print(i)
        break

    if i == num:
        print('0')
        break
