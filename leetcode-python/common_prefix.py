from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for i in strs:
            
            if not i.startswith(common_prefix):
                while (i.startswith(common_prefix)) == False:
                    if len(common_prefix) == 1:
                        common_prefix = ""
                    else:
                        common_prefix = common_prefix[0:-1]
                
                
        return common_prefix


Solution().longestCommonPrefix( strs = ['c', 'acc', 'ccc'])