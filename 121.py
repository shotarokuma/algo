class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        dp = [0 for _ in range(m)]
        maxI = prices.index(max(prices))
        minV = float('inf')
        for i in range(m - 1):
            if minV <= prices[i]:
                continue
            if maxI < i:
                maxI = prices.index(max(prices[i:]))
            dp[i] = prices[maxI] - prices[i]
            minV = prices[i]
        return max(dp)

        
    def sample(self, prices):
        left = 0
        right = 1
        max_profit = 0
        while(right < len(prices)):
           currentProfit = prices[right] - prices[left] 
           if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
           else:
                left = right
           right += 1
        return max_profit
