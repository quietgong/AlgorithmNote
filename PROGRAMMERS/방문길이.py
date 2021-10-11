def solution(dirs):
    visited=set()
    x,y=0,0
    for dir in dirs:
        if dir=="L":
            nx=x
            ny=y+1
        elif dir=="R":
            nx = x
            ny = y-1
        elif dir == "U":
            nx = x+1
            ny = y
        elif dir == "D":
            nx = x-1
            ny = y
        if -5<=nx<=5 and -5<=ny<=5:
            go=(x,y,nx,ny)
            back=(nx,ny,x,y)
            x,y=nx,ny
            if go not in visited:
                visited.add(go)
                visited.add(back)
    return len(visited)//2

# 경로탐색이 아닌, 경로가 있었는지 없었는지 여부를 확인하는 문제, set 자료형을 사용하면 쉽게 풀린다.