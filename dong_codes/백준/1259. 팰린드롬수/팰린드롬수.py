import sys
num = ''
num_list = []
while num != '0' :
    num_list.append(num)
    num = sys.stdin.readline().rstrip()
num_list = num_list[1:]

for number in num_list :
    check = True
    number_length = len(number)
    check_length = number_length // 2

    for i in range(check_length) :
        if number[i] != number[-i-1] :
            check = False
    if check == True :
        print('yes')
    else :
        print('no')
