class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0

        i = l - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        
        j = i
        while j >= 0 and s[j] != " ":
            j -= 1
        
        return i - j
