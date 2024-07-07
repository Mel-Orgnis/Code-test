import sys
n = int(sys.stdin.readline().rstrip())

A = list(map(int,sys.stdin.readline().split()))
A = set(A)

m = int(sys.stdin.readline().rstrip())
M = list(map(int,sys.stdin.readline().split()))
for ms in M :
    if ms in A :
        print(1)
    else :
        print(0)
