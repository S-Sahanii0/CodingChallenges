class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)
        
        while x != 0: 
            pop = x % 10
            x /= 10
            if rev > max_int/10 or rev == max_int/10 and pop >7:
                return 0
            if rev < min_int/10 or rev == min_int/10 and pop < -8:
                return 0
            rev = rev * 10 + pop
        
            return rev
    
