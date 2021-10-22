class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        while ans * ans <= x:
            ans += 1
        print(ans-1)
        return ans - 1
    

Solution().mySqrt(x = 4)

