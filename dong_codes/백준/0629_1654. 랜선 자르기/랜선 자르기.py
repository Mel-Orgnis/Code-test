import sys
K_N = sys.stdin.readline().rstrip().split(' ')
K = int(K_N[0])
N = int(K_N[1])
LAN = []
for i in range(K) :
    temp_lan = int(sys.stdin.readline())
    LAN.append(temp_lan)
def check_N(lan_list,n) :
    start = 1
    end = max(lan_list) 
    while start <= end :
        mid = (start + end) // 2
        divided_lan = 0
        for lan in lan_list :
            divided_lan += (lan // mid)
        if divided_lan < n :
            end = mid - 1
        elif divided_lan >= n :
            start = mid +1
    return end

print(check_N(LAN,N))
