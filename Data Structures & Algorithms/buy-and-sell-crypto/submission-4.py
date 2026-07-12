class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        for i in range(len(prices)):
            for j in range(i,len(prices),1):
                profit=prices[j]-prices[i]
                if profit>maximum:
                    maximum=profit
        return maximum



        