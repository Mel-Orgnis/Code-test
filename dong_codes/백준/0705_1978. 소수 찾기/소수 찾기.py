import sys
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
sup = int(1000**(1/2))

for i in range(2,sup+1) :
    numbers = [number for number in numbers if (number % i != 0 or number / i == 1) and number != 1]
print(len(set(numbers)))