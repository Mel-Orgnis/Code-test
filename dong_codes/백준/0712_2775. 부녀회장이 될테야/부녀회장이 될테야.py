import sys

now_people = list(range(1,15))
people_list = [now_people]

for i in range(14) :
    next_people = [1]
    for j in range(13) :
        next_people.append(now_people[len(next_people)] + next_people[-1] )
    people_list.append(next_people)
    now_people = next_people

T = int(sys.stdin.readline())

for i in range(T) :
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(people_list[k][n-1])