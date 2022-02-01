


class Solution:
    def climbStairs(self, n: int) -> int:
        onesAndtwos = list(divmod(n , 2))
        if onesAndtwos[1] != 0:
            countOfSteps = [1]
        else:
            countOfSteps = []
        
        if onesAndtwos[0] % 2 == 0:
                while onesAndtwos[0] != 0:
                    countOfSteps.append(2)
                    onesAndtwos[0] = onesAndtwos[0] - 2
        else:
                while onesAndtwos[0] != 1:
                    countOfSteps.append(2)
                    onesAndtwos[0] = onesAndtwos[0] - 2
                countOfSteps.append(1)
        print(countOfSteps)
       
        onlyTwo = list(filter(lambda x: x % 2 == 0, countOfSteps))
       
        result = len(countOfSteps)
        for i in range(1, len(onlyTwo)-1):
            result = result + 2
            
            
        print(result)
        return result
   
Solution().climbStairs(n=5)
        
    
       