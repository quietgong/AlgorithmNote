T = int(input())
arr = []
#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = [0] * 26
for i in range(T):
    name = input()
    arr.append(name[0])

arr = str(arr)

for i in range(len(alphabet)):
    if arr.count(alphabet[i]) >= 5:
        res[i] = 1

if(sum(res)==0):
    print("PREDAJA")
else:
    for i in range(len(res)):
        if res[i] != 0:
            print(alphabet[i], end='')