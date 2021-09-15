def solution(s):
    ans = []
    res = ''
    for i in s:
        ans.append(ord(i))
    ans.sort(reverse=True)
    for i in ans:
        res += chr(i)
    return res

# 문자->아스키코드 ord('A')=65
# 아스키코드->문자 chr(65)='A'
