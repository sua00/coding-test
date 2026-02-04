def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        candidate = -1
        for i in range(s, e+1):
            if arr[i] > k:
                if candidate == -1 or arr[i] < candidate:
                    candidate = arr[i]
        answer.append(candidate)
    return answer