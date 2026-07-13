class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxP=0
        n=len(heights)
        for i in range(n):
            for j in range(i,n):
                maxP=max((j-i)*(heights[j] if heights[j]<heights[i] else heights[i]),maxP)
        return maxP
        