from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = nums.count(val)
        for i in range(length):
                nums.remove(val)
        return len(nums)

Solution().removeElement(nums=[3,3,2,2], val=3)