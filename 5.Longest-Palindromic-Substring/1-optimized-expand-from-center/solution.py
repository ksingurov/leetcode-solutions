# version which returns lenght of longest palindrome, we need a palindrome itself

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def max_possible_lenght(i):
            return 2 * (len(s) - i) - 1

        def palindrome_lenght(i, parity):
            p_len = parity 
            i_left = i - parity
            i_right = i + 1
            while i_left > -1 and i_right < len(s) and s[i_left] == s[i_right]:
                p_len += 2
                i_left -= 1
                i_right += 1
            return p_len
            
        max_lenght = 1
        middle = len(s) // 2
        i = middle
        n = 0
        while -1 < i < len(s):
            odd_palindrome_lenght = palindrome_lenght(i, 1)
            even_palindrome_lenght = palindrome_lenght(i, 0)
            print(f"i: {i} | odd: {odd_palindrome_lenght} | even: {even_palindrome_lenght}")
            max_lenght = max(max_lenght, odd_palindrome_lenght, even_palindrome_lenght)
            n += 1
            i = middle + (-1)**(n + 1) * ((n + 1) // 2)

        return max_lenght


s = "babad"
# s = "babab"
# s = "abba"
# s = "abbcbba"
# s = "abbcbbax"
# s = "bbabbcbbax"
# s = "cbbd"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
