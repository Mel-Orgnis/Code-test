def quater(n,r,c) :
    if r < 2**(n-1) :
        y = 1
    else :
        y = -1
    if c < 2**(n-1) :
        x = -1
    else : 
        x = 1
    
    if x == -1 and y == 1 :
        return 0
    elif x == 1 and y == 1 :
        return 1
    elif x == -1 and y == -1 :
        return 2
    elif x == 1 and y == -1 :
        return 3

def find_order(n,r,c) :
    value = 0
    for i in range(n) :
        mini_n = i+1
        mini_r = r%2**mini_n
        mini_c = c%2**mini_n
        value += quater(mini_n,mini_r,mini_c)* 4**(mini_n-1)
    return value
line = list(map(int,input().rstrip().split()))
print(find_order(line[0],line[1],line[2]))