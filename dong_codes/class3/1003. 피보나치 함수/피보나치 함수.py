import sys
n = int(sys.stdin.readline())
fib_list = [[0,0] for _ in range(41)]
fib_list[0] = [1,0]
fib_list[1] = [0,1]
for i in range(2,41):
    fib_list[i][0] = fib_list[i-1][0] + fib_list[i-2][0]
    fib_list[i][1] = fib_list[i-1][1] + fib_list[i-2][1]
for i in range(n) :
    test_case = int(sys.stdin.readline())
    print(fib_list[test_case][0],end=' ')
    print(fib_list[test_case][1])
