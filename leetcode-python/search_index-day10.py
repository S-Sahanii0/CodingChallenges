class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        for i in range(nums.length):
            if nums[i] == target:
                return i
            