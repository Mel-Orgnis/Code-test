import sys
def num_list(n=4) :
    return [[n_slice for n_slice in f'{num:04d}'] for num in range(10**4)]
def insert_six(n=4) :
    numbers = num_list(n)
    result_set = set()
    for i in range(n+1) :
        for number in numbers :
            inserted_six = number.copy()
            inserted_six.insert(i,'666')
            six_num = ''.join(inserted_six)
            result_set.add(int(six_num))
    result_set = list(result_set)
    result_set.sort()
    return result_set

title_Nth = int(sys.stdin.readline().rstrip()) - 1
title_list = insert_six()

print(title_list[title_Nth])
    
