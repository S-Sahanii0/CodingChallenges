from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            i ^= num
        return i

Solution().singleNumber(nums=[1,1,2,2,3,4,3])