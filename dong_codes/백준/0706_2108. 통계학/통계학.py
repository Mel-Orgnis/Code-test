import sys
N = int(sys.stdin.readline())
numbers = []
for i in range(N) :
    m = int(sys.stdin.readline())
    numbers.append(m)
numbers.sort()
print(round(sum(numbers)/len(numbers)))
print(numbers[int(len(numbers)/2 -0.5)])

num_dic = {}
for num in numbers :
    if not (num in num_dic) :
        num_dic[num] = 1
    num_dic[num] +=1
many_num = [k for k,v in num_dic.items() if max(num_dic.values()) == v]
if len(many_num) >= 2 :
    many_num.sort()
    print(many_num[1])
else :
    print(many_num[0])
max_num = max(numbers)
min_num = min(numbers)
if N == 1 :
    print(0)
else :
    print(max_num-min_num)