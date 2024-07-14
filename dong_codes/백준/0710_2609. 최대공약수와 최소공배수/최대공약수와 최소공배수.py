n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])
sup = min(n,m) 

gcd = 1
for i in range(2,sup+1) :
    if n % i + m % i == 0 :
        gcd = i
lcm = int(m*n / gcd)

print(gcd)
print(lcm)