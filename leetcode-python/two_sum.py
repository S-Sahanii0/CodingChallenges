class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create an empty hashmap.
        hashmap = {}

        #We can use the enumerate method in our for loop to easily acess nums[i] through the n variable.
        for i,n in enumerate(nums):

            #We need to find the difference between the current nums array value and our given target, so we can search for this value in the hashmap later.
            #Example. d = 6-2 ---> we need to search for the 4 in the hashmap.
            d = target - n
            
            #Searches for the difference in the hashmap.
            if d in hashmap:
                
                #If the difference is found as a key value in the hashmap then we return the value associated with the difference, which is the difference's index. We also need to return our current index.
                return [hashmap[d], i]
                
                #If the difference can't be found in the hashmap, then we can store the current n value and index, so we can use it for later loop iterations.
            else:
                hashmap[n] = i
        return
Solution.twoSum(Solution, [3,2,3], 6)
                
            