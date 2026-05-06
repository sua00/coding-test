def solution(num_list):
    answer = []
    cnt = 0
    for i in num_list:
        if i %2 ==0:
            cnt= cnt+1
        else:
            continue
    answer.append(cnt)
    answer.append(len(num_list)-cnt)
    return answer