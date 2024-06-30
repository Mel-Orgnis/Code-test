#N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

import sys
N = int(sys.stdin.readline())
num = 1
check = 0
for i in range(N) :
    num *= (i+1)
    num = str(num)
    while num[-1] == '0':
        check +=1
        num = num[:-1]
    num = int(num)

print(check)

