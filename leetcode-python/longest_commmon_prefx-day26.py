from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        k = 0
        while k < len(strs[0]):
            c = strs[0][k]
            for i in range(1, len(strs)):
                if k >= len(strs[i]) or c != strs[i][k]:
                    return s
            s += c
            k += 1
        return s