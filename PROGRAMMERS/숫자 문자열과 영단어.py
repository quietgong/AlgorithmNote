def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(word)):
        s = s.replace(word[i], str(i))
    answer = int(s)
    return answer

# 입출력 예
# s	                    result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"	234567
# "123"	                123