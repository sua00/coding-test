def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        elif arr[i] == arr[i-1]:
            continue
        else:
            answer.append(arr[i])
    return answer