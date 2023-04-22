class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_string = len(s)
        if l_string == 0:
            return 0
        
        p_substring = s[1]
        for l_substring in range(1, l_string + 1):
            for i in range(l_string - l_substring):
                substring = s[i:i + l_substring]
                if substring == substring[::-1]:
                    p_substring = substring
                    break
        return p_substring

