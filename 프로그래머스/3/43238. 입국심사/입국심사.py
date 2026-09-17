# 경계값을 찾는 문제가 이분 탐색 문제
# 해당 문제의 경우도 몇분에서 모두 심사가 가능해지는지 찾아야함
# 어떤 값 x를 정했을 때 가능/불가능을 판단할 수 있음 -> 이런게 이분 탐색 시그널
def solution(n, times):
    answer = 0
    
    left = 1 #범위의 최솟값
    right = max(times) * n #최대의 시간이 걸리는 사람이 n명을 모두 심사할 때 (60)
    
    while left < right:
        mid = (left+right)//2 #30 
        
        people = 0
        for time in times:
            people += (mid//time) #30//7 = 4, 30//7 =3 -> 7명 평가 가능
        
        if people >= n:
            right = mid #최대 범위를 줄임
        else:
            left = mid+1 #시간이 모자라면 더 큰 범위의 반쪽에서 탐색 마저해야함
        
    
    return left