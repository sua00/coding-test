def solution(n):
    
    # def fin(n):
    #     if n <=1:
    #         return n
    #     else:
    #         return fin(n-2)+fin(n-1)
    # 그냥 이렇게 구현하면 시간 복잡도 초과함 -> DP가 필요한 이유
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] =1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]%1234567