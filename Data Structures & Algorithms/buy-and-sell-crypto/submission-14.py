class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        min=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>min:
                maxP=max(prices[i]-min,maxP)
            else:
                min=prices[i]
        return maxP





        