from collections import deque

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            num_bin = deque((bin(number)[2:]))
            num_bin.appendleft('0')
            for i in range(len(num_bin) - 1, -1, -1):
                if num_bin[i] == '0':
                    num_bin[i] = '1'
                    num_bin[i + 1] = '0'
                    break
            answer.append(int('0b' + ''.join(num_bin), 2))
    return answer
# 홀수인 경우 제일 끝에서 0을 찾아 1로 바꾸고 그 위치의 바로 앞의 숫자를 0으로 바꾼다. (1이면 비트2개가 달라지고 0이면 비트1개가 달라지므로)