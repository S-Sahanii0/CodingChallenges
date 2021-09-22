class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        rev = 0
        forward = x
        while x!=0:
            
            pop = x % 10
            x = x//10
            rev = rev*10+pop
             
        if(rev >= pow(2,31)-1 or rev < pow(-2,31)):
            rev = 0
        return rev == forward
            
       

Solution().isPalindrome(121)
            
            



            