class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
               
                return i
            if i != len(nums) - 1:
                if nums[i] < target < nums[i+1]:
                    return i+1
        if target < nums[len(nums) - 1]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
       
            