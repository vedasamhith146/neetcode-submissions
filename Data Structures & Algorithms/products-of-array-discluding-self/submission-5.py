class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       output_array=[]
       for i in range(len(nums)):
        prod=1
        for j in range(len(nums)):
            if j!=i:
                prod*=nums[j]
        output_array.append(prod)
        
       return output_array
        