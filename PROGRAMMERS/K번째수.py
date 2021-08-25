def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = [0]*3
        command = commands[i]
        i,j,k = command[0], command[1], command[2]
        arr = array[i - 1:j]
        arr.sort()
        answer.append(arr[k - 1])
    return answer

# 입출력 예
# array	                commands	                        return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]