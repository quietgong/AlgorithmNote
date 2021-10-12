def solution(skill,skill_tree):
    ans=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            ans+=1
    return ans

# 구현.. (배열)