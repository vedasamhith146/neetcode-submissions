class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        output=[]
        for k in range(n):
            target=-nums[k]
            seen=set()
            for i in range(n):
                if i!=k:
                    if target-nums[i] in seen:
                        small_array=[nums[i],target-nums[i],-target]
                        if sorted([nums[i],target-nums[i],-target]) not in output:
                            output.append(sorted([nums[i],target-nums[i],-target]))
                    seen.add(nums[i])

        return output



        