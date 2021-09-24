from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        print(nums)
        print(len(nums))
        return len(nums)

   

Solution().removeDuplicates(nums=[1,1,2])

#Another Solution:
def removeDuplicates(self, nums: List[int]) -> int:

        length = 0
        if len(nums) == 0: return length
        for i in range(1,len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length+1
        