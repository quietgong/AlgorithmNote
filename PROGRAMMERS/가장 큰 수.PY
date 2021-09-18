def solution(numbers):
    ans=''
    info=[]
    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])
        info.append([numbers[i],numbers[i]*3])
    info.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(info)):
        ans+=info[i][0]
    return str(int(ans))

# 문자열의 sorting은 앞자리의 아스키코드를 비교해가면서 정렬한다.
# ex) 121 와 12 이 있을때, 121*3=121121121, 12*3=121212
# 첫째 자리부터 세번째 자리까지는 정렬기준이 없음. 네번째 자리부터 121*3의 1보다 12*3의 2가 더 크므로
# 12가 121보다 먼저 와야함.
# 마지막 int 자료형을 해주는 이유는 numbers가 모두 0일 때 ans가 0000 이 될 수 있기 때문에 예외처리 해주는것.