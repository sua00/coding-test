def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0],command[1], command[2]
        #print(i,j,k)
        arr_ = array[i-1:j]
        arr_ = sorted(arr_)
        answer.append(arr_[k-1])
    return answer