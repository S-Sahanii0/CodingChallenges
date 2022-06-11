from operator import mod


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ht = {"}": "{", ")": "(", "]": "["}
        
        for p in s:
            if p in ht.values():
                stack.append(p)
            elif p in ht:
                if len(stack) == 0 or stack[len(stack) - 1] != ht[p]:
                    return False
                stack.pop()
        return len(stack) == 0