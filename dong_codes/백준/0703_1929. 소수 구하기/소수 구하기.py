import sys
M_N = list(map(int,sys.stdin.readline().split()))
M = M_N[0]
N = M_N[1]

sup = max(int(N**(1/2)),2)
num_list = list(range(M,N+1))
for i in range(2,sup+1) :
    num_list = [num for num in num_list if (num%i !=0 or num/i == 1) and num !=1]
for num in num_list :
    print(num)