def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i]) # 다루기 쉽게 문자열을 리스트로 변환
    while True:
        remove = [[0] * n for _ in range(m)] # 지워진 위치를 저장하기 위해 remove 리스트 사용
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == \
                        board[i + 1][j + 1]: # 2x2 배열이 모두 같으면
                    remove[i][j], remove[i][j + 1], remove[i + 1][j], remove[i + 1][j + 1] = 1, 1, 1, 1
        cnt = 0
        for i in range(m):
            cnt += sum(remove[i])
        answer += cnt
        if cnt == 0: # 사라지는 블록이 없으면 반복문 종료
            break
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if remove[i][j] == 1:
                    x = i - 1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1

    return answer