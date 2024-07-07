N = int(input())
if N == 1 :
    print(1)
else :
    check = 0
    while N >= 2**(check)+1 :
        check += 1
    N -= 2**(check-1)

    print(2*(N))
