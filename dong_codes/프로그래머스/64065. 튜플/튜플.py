def solution(s):
    splited_list = s.split('}')
    listed_list = []
    for string in splited_list :
        string = [char for char in string if char.isdigit() or char ==',']
        string = ''.join(string).split(',')
        string = [int(s) for s in string if s!='']
        listed_list.append(string)
    listed_list = listed_list[:-2]
    final_list = []
    
    len_list = []
    for lists in listed_list :
        len_list.append(len(lists)-1)
    for i in range(len(listed_list)):
        final_list.append(listed_list[len_list.index(i)])
    
    answer = []

    for i in range(len(final_list)) :
        for j in range(len(final_list[i])) :
            if final_list[i][j] not in answer :
                answer.append(final_list[i][j])

    return answer
