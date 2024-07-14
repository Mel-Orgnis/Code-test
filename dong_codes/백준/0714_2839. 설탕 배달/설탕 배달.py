num = int(input())
check = True

if num % 5 == 0 :
    answer = int(num / 5)
else :
    five = num // 5
    while check :
        remain = num - (five*5)
        if remain % 3 == 0 :
            three = remain / 3
            answer = int(five + three)
            break
        five -=1
        if five < 0 :
            check = False
if check :
    print(answer)
else :
    print(-1)