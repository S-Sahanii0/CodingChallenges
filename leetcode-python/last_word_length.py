class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_words = s.split()
        last_word = list_of_words[len(list_of_words) - 1]
        return (len(last_word))
        