def solution(n):
    base=''
    ans=0
    while n>0:
        n,q=divmod(n,3)
        base+=str(q)
    base=base[::-1]
    for i in range(len(base)):
        ans+=int(base[i])*(3**i)
    return ans

# [::-1], divmod