import sys
w_l = [0] * 52
s_l = [0] * 52
ans = 0
n, m = map(int, input().split())
w = sys.stdin.readline().rstrip()
s = sys.stdin.readline().rstrip()
for i in range(n):
    if 'a' <= w[i] <= 'z':
        w_l[ord(w[i]) - ord('a')] += 1
    else:
        w_l[ord(w[i]) - ord('A') + 26] += 1

start, length = 0, 0
for i in range(m):
    if 'a' <= s[i] <= 'z':
        s_l[ord(s[i]) - ord('a')] += 1
    else:
        s_l[ord(s[i]) - ord('A') + 26] += 1
    length += 1
    if length == n:
        if w_l == s_l:
            ans += 1
        if 'a' <= s[start] <= 'z':
            s_l[ord(s[start]) - ord('a')] -= 1
        else:
            s_l[ord(s[start]) - ord('A') + 26] -= 1
        length -= 1
        start += 1
print(ans)

# 슬라이딩 윈도우, 아스키코드 활용
# 아이디어 : s의 부분 문자열이 w의 길이와 같고 w의 알파벳 출현과 같으면 w의 순열이 된다.