from operator import mod


class Solution:
    def isValid(self, s: str) -> bool:
        # opening_brackets = []
        # ending_brackets = []
        # for i in s:
        #     if i == '(' or i == '[' or i == '{':
        #         opening_brackets.append(i)
        #     if i == ')' or i == ']' or i == '}':
        #         ending_brackets.append(i)
        # if len(opening_brackets) != len(ending_brackets):
        #     return False
        # else:
        #     try:
        #         for j in range(len(opening_brackets)):
                    
        #             if opening_brackets[j] == '(' and ending_brackets[j] == ')':
        #                 ending_brackets.remove(ending_brackets[j])
        #                 opening_brackets.remove(opening_brackets[j])
        #             if opening_brackets[j] == '[' and ending_brackets[j] == ']':
        #                 ending_brackets.remove(ending_brackets[j])
        #                 opening_brackets.remove(opening_brackets[j])

        #             if opening_brackets[j] == '{' and ending_brackets[j] == '}':
        #                 ending_brackets.remove(ending_brackets[j])
        #                 opening_brackets.remove(opening_brackets[j])
        #     except:
        #         return ending_brackets == [] and opening_brackets == []
        if mod(len(s), 2) == 1:
            return False
        brackets = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                brackets.append(i)
            print(len(brackets))
            if len(brackets) != 0:
                
                if i == ')' or i == ']' or i == '}':
                    if brackets[-1] == '(' and i == ')':
                        brackets.pop()
                    if brackets[-1] == '[' and i == ']':
                        brackets.pop()
                    if brackets[-1] == '{' and i == '}':
                        brackets.pop()
        return brackets == []
                

    
Solution().isValid(s = "([}}])")

            