class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        seen=set()
        maxL=0
        while l<=r and r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                maxL=max(len(seen),maxL)
                r+=1
            else:
                while s[r] in seen:
                    print(seen)
                    print(f"Current value of r={r},l={l}, Removing {s[l]}")
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
                r+=1

        return maxL

            


        
       

