from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num = set(nums)
        n = len(num)
        for i in range(1, n+1):
            if i not in num:
                return i
				
        return i + 1
    
    


Solution().firstMissingPositive(nums=[3,4,-1,1])