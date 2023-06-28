class Solution:
    def longestPalindrome(self, s: str) -> str:

        small_palindromes = []
        middle = len(s) // 2
        i = middle
        n = 0
        while -1 < i < len(s):
            # print(i)
            try:
                if s[i] == s[i + 1]:
                    # small_palindromes.append(('even', i))
                    small_palindromes.append((0, i))
            except:
                pass
            try:
                if s[i - 1] == s[i + 1]:
                    # small_palindromes.append(('odd', i,))
                    small_palindromes.append((1, i,))
            except:
                pass
            n += 1
            i = middle + (-1)**(n + 1) * ((n + 1) // 2)

        return small_palindromes


s = "babad"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
