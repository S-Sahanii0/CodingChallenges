class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        else:
            length_of_needle = len(needle)

            for i in range(len(haystack)):
                sub_string = haystack[:length_of_needle]
                if sub_string == needle:
                    return i
                else:
                    haystack = haystack[1:]
                    
                
                

Solution().strStr(haystack="hello", needle= "ll")