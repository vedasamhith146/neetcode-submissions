class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       pref=[0]*len(nums)
       suff=[0]*len(nums)
       pref[0]=suff[len(nums)-1]=1
       output_array=[0]*len(nums)
       for i in range(1,len(nums)):
        pref[i]=nums[i-1]*pref[i-1]
       for i in range(len(nums)-2,-1,-1):
        suff[i]=nums[i+1]*suff[i+1]
       for i in range(len(nums)):
        output_array[i]=pref[i]*suff[i]
       return output_array




        