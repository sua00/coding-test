# 1칸 또는 2칸 이동 가능
# 맨마지막에 1칸 남거나 2칸 남거나
#dp[n] = dp[n-1] + dp[n-2]
def solution(n):
    answer = 0
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-2]+dp[i-1]
    
    answer = dp[n] % 1234567
    
    return answer