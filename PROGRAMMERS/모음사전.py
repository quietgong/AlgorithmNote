from itertools import product
def solution(word):
    letter=['A','E','I','O','U']
    arr=[]
    for i in range(1,6):
        for x in product(letter,repeat=i):
            arr.append(''.join(list(x)))
    arr.sort()
    return arr.index(word)+1

# 중복 순열