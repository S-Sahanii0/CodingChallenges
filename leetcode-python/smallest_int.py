from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        haha = list(set(nums))
        result = nums[-1] + 1
        i = 0
        if nums[-1] > 0:
            
            while i< len(haha)-1 and haha[i+1] != (haha[i]+1):
                result = haha[i]+1
            print(result)
            return result
        else:
            print(1)
            return 1


Solution().firstMissingPositive(nums=[3,4,-1,1])