def maxProfit(k, prices):
    '''Returns the maximum profit you can achieve at most k transactions.'''
    n = len(prices)
    
    if k <= 0 or n < 2:
        return 0
    
    # k is big enough to cover all possibilities
    if k > n/2:
        return sum(i-j for i, j in zip(prices[1:], prices[:-1]) if i-j>0)
    
    # Initialize table for storing data (bottom-up approach)
    dp = [[0]*n for _ in range(k+1)]
    
    # Time complexity O(k*n)
    for i in range(1, k+1):
        effectiveBuyPrice = prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] - effectiveBuyPrice)
            effectiveBuyPrice = min(effectiveBuyPrice, prices[j] - dp[i-1][j])
    return dp[k][n-1]

