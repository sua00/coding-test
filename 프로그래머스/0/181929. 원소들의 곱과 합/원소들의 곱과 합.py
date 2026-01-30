def solution(num_list):
    answer = 0
    multi = 1
    for i  in num_list:
        multi *= i
    if multi > (sum(num_list)*sum(num_list)):
        answer = 0
    else :
        answer =1
    return answer