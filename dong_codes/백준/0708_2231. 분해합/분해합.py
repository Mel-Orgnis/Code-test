def make_N(N) :
    digit_length = len(str(N))
    answer = N
    inf = digit_length * 9
    for i in range(inf) :
        M = max(1,N - (i+1))
        M_length = len(str(M))
        M_sum = M
        for j in range(M_length) :
            M_sum += int(str(M)[j])
        if M_sum == N :
            answer = min(answer,M)
    if answer == N :
        print(0)
    else :
        print(answer)

make_N(int(input()))
