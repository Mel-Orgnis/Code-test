import sys
sys.setrecursionlimit(100000000)
def BFS_bachu(x,y,bat):
    if bat[y][x] == 1:
        bat[y][x] = 0
        if y < len(bat) -1 :
            BFS_bachu(x,y+1,bat)
        if y > 0 :
            BFS_bachu(x,y-1,bat)
        if x < len(bat[0]) - 1: 
            BFS_bachu(x+1,y,bat)
        if x > 0 :
            BFS_bachu(x-1,y,bat)
        return 1
    return 0
    

T = int(input())
for _ in range(T) :
    bat_list = list(map(int,input().rstrip().split()))
    x = bat_list[0]
    y = bat_list[1]
    K = bat_list[2]
    bachu_position = []
    for _ in range(K) :
        bachu = list(map(int,input().rstrip().split()))
        bachu_position.append(bachu)
    bachubat = [[0 for _ in range(x)] for _ in range(y)]
    for i in range(len(bachu_position)):
        bachubat[bachu_position[i][1]][bachu_position[i][0]] = 1
    count = 0

    for y in range(len(bachubat)):
        for x in range(len(bachubat[0])):
            count += BFS_bachu(x,y,bachubat)
    
    print(count)