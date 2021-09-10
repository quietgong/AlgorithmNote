def solution(n):
    k=n
    while True:
        k+=1
        if bin(n).count("1")==bin(k).count("1"):
            break
    return k

# bin 연산자 (2진수 변환)