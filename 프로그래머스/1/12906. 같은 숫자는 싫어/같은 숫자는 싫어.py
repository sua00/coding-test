def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    nums = []
    nums.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        else : 
            nums.append(arr[i+1])
    return nums
    
    