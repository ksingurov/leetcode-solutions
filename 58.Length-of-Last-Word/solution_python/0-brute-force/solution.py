# Solution with built-in string functions

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])
