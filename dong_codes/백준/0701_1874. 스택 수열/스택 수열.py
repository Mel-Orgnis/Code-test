now = 1

stk = []
check = True
ans = []

n = int(input())

for i in range(n) :
    num = int(input())
    while now <= num :
        stk.append(now)
        ans.append('+')
        now +=1
    if stk[-1] == num :
        stk.pop()
        ans.append('-')
    else :
        check = False
if check : 
    for a in ans :
        print(a)
else :
    print('NO')