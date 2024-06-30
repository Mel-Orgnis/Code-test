import sys
num_of_subject = int(sys.stdin.readline().rstrip())
grade_list = [int(grade) for grade in sys.stdin.readline().rstrip().split(' ')]

best_grade = max(grade_list)
for i in range(num_of_subject) :
    grade_list[i] = float(grade_list[i]) / float(best_grade) * 100
mean_grade = sum(grade_list) / num_of_subject
print(mean_grade)