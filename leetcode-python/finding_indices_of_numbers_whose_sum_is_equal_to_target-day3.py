from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashMap:
                print( [hashMap[difference], i]) 
                return [hashMap[difference], i]
            hashMap.update({num:i})

        

Solution().twoSum(nums =[1,2,3,4], target = 7)
      
    