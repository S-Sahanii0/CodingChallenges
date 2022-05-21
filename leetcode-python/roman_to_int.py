class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        list_of_letters = list(s)
        result = 0 
        for i in range(len(list_of_letters) - 1):
            key = list_of_letters[i]
            if i != len(list_of_letters) - 1:
                next_key = list_of_letters[i + 1]
                if roman_map[key] < roman_map[next_key]:
                    result -= roman_map[key]
                else:
                    result += roman_map[key]
            else:
                result += roman_map[key]
        return result
            