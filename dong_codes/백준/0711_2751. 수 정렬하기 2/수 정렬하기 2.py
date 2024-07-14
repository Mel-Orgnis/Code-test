import sys
n = int(sys.stdin.readline())
n_list = []
for i in range(n) :
    line = int(sys.stdin.readline())
    n_list.append(line)
n_list.sort()

for num in n_list :
    print(num)