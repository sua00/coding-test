#최종적으로는 n-2에서 +2 점프 1번
#또는 n-1에서 +1 점프 1번
#즉 dp[n] = dp[n-1]+dp[n-2]
#dp[1] = 1
#dp[2] = 2

def solution(n):
    answer = 0
    dp = [0]*(n+2)
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+2):
        dp[i]= dp[i-1]+dp[i-2]
    
    answer = dp[n]%1234567
    return answer