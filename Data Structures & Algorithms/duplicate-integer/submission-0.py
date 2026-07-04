class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(len(nums)):
            if nums[i]  in seen:
                return True
            seen.add(nums[i])
        return False


solution=Solution()
output=solution.hasDuplicate(nums=[1,2,3,4])
print(output)


        