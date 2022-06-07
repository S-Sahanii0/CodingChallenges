from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for i in range(len(nums)):
            if i in result:
                result.pop(i)
            else:
                result[i] = nums[i]
        return result.values()[0]