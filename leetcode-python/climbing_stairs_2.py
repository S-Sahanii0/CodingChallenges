class Solution:
    mem = {}
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        else:
            if n not in self.mem:
                self.mem[n] =  self.climbStairs(n-2) + self.climbStairs( n-1)
        return self.mem[n]
            