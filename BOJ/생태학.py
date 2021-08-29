import sys
from collections import defaultdict
trees = defaultdict(int)
total = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    trees[tree] += 1
    total+=1

tree_list = list(trees.keys())
tree_list.sort()

for tree in tree_list:
    print('%s %.4f' %(tree, trees[tree]/total*100))
    
# 포인트 : defaultdict 사용법, 입력이 없을때까지 입력받기, print 표기법