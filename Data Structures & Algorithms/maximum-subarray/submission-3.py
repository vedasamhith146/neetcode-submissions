class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        sum_front=0
        sum_back=0
        while i<j:
            sum_front+=nums[i]
            sum_back+=nums[j]
            if sum_front>=0 and sum_back>=0:
                i+=1
                j-=1
            else:
                if sum_front<sum_back:
                    nums=nums[i+1:]
                else:
                    nums=nums[:-(i+1)]
                i=0
                j=len(nums)-1
                sum_front=0
                sum_back=0

        return sum(nums)

