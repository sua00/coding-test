def solution(arr):
    answer = []
    #print(dir(list))
    for i in range(len(arr)):
        if len(answer)==0:
            answer.append(arr[i])
        elif arr[i] != answer[-1]:
            answer.append(arr[i])
        else:
            continue
        
    return answer