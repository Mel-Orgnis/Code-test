N = int(input())

def nth_line(n) :
    epsilon = 10**(-5)
    kth = (n -1 ) / 6
    answer = -(1/2) + ((1+8*kth)**(1/2))/2
    return answer - epsilon
print(int(nth_line(N)+2))