word = str(input())
crotian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(crotian)):
    if crotian[i] in word:
        word = word.replace(crotian[i], "a") # 크로아티아 알파벳을 a라는 한글자로 치환해버린다.

print(len(word))