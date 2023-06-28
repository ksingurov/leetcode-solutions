from math import ceil

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def len_p(a, b):
            return b - a + 1
        
        def max_possible_len(parity, i):
            if i < len(s) / 2:
                return 2 * (i + 1) - parity
            else:
                return 2 * (len(s) - i - 1) + parity
            
        len_max = 1
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

        print(small_palindromes)
        for p in small_palindromes:
            if max_possible_len(p[0], p[1]) < len_max:
                break
            print(p)
            # d = 0 if p[0] == 'even' else 1 # odd/even
            parity = p[0]
            j = 0
            # print(p[1] - d - j, p[1] + 1 + j, s[p[1] - d - j], s[p[1] + 1 + j])
            while p[1] - parity - j > -1 and p[1] + 1 + j < len(s) and s[p[1] - parity - j] == s[p[1] + 1 + j]:
                len_max = max(len_max, len_p(p[1] - parity - j, p[1] + 1 + j))
                # print(p[1], p[1] - d - j, p[1] + 1 + j)
                j += 1

        return len_max

# s = "babad"
# s = "babab"
# s = "abba"
# s = "abbcbba"
# s = "abbcbbax"
s = "bbabbcbbax"
# s = "cbbd"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
