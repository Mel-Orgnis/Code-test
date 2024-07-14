import sys
N_M = list(map(int,sys.stdin.readline().split(' ')))
N = N_M[0]
M = N_M[1]
nums = list(map(int,sys.stdin.readline().split(' ')))
target = M
error = target
for i in range(len(nums)) :
    numbers = list(nums)
    first = numbers.pop(i)
    for j in range(len(numbers)) :
        numbers_poped = list(numbers)
        second = numbers_poped.pop(j)
        for k in range(len(numbers_poped)) :
            numbers_poppoped = list(numbers_poped)
            third = numbers_poppoped.pop(k)
            num_sum = first + second + third
            if num_sum <= target :
                error = min(error, target - num_sum)
print(target-error)             
