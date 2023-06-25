class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_string = len(s)

        # small_palindromes = [] # elem: (len, i)
        palindromes = {2: set(), 3: set()} # dict[int, set[int]]
        for start in range(l_string - 2):
            if s[start: start + 2] == s[start: start + 2][::-1]:
                    # small_palindromes.append((2, start))
                    palindromes[2].add(start)
            try:
                if s[start: start + 3] == s[start: start + 3][::-1]:
                    # small_palindromes.append((3, start))
                    palindromes[3].add(start)
            except:
                pass

        return palindromes


s = "babad"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
