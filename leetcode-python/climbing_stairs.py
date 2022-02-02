


class Solution:
    def climbStairs(self, n: int) -> int:
        # easy to understand: bottom-up solution
        if n < 3:
            return n
        x, y = 1, 2
        for i in range(n - 2):
            x, y = y, x + y
        return y

   
Solution().climbStairs(n=1)
        
    
       