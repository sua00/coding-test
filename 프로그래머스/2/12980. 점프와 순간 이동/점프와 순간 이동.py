#K칸 점프 : k만큼 건전지 소모
#온거리 *2의 순간이동 : 건전지 x

def solution(n):
    ans = 0
    
    while n > 0:
        if n%2 ==0:
            n=n//2
            continue
        else:
            n = n-1
            ans +=1

    return ans