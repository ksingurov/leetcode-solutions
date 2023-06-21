class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_string = len(s)
        if l_string == 0:
            return 0
        
        p_substring = s[1]
        for l_substring in range(2, l_string + 1):
            for i in range(l_string + 1 - l_substring):
                substring = s[i:i + l_substring]
                if substring == substring[::-1] and len(substring) > len(p_substring):
                    p_substring = substring
        return p_substring
    

if __name__ == "__main__":
    sol = Solution()
    s = "bbabbcbbax"
    res = sol.longestPalindrome(s)
    print(res)
