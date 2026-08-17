class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=max(prices)
        res=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            res=max(res,prices[i]-mini)
        return res