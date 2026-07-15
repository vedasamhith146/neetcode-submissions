class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        output=[]
        max_element=max(nums[:r+1])
        output.append(max_element)
        for i in range(r+1,len(nums)):
            l+=1
            curr_max=max(nums[l:i+1])
            output.append(curr_max)
        
        return output
                
            



        