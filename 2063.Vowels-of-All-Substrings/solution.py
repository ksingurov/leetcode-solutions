import re

class Solution:
    def countVowels(self, word: str) -> int:
        substrings = []
        for string_lenght in range(1, len(word) + 1):
            for i in range(len(word) - string_lenght + 1):
                substrings += [word[i:i + string_lenght]]

        res = 0
        for substring in substrings:
            res += len(re.findall("a|e|i|o|u", substring))

        return res
