

class Solution:

    def isUgly(self, n: int) -> bool:
        while n % 2 == 0 and n > 1:
            n //= 2
        
        while n % 3 == 0 and n > 1:
            n //= 3

        while n % 5 == 0 and n > 1:
            n //= 5
        
        print(n==1)
        return n == 1


