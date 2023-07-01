# since we need a palindrome itself, inner function is adjusted to return lenght and palaindome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def max_possible_lenght(i):
            return 2 * (len(s) - i) - 1

        def palindrome(i, parity):
            # p_len = parity 
            i_left = i - parity
            i_right = i + 1
            while i_left > -1 and i_right < len(s) and s[i_left] == s[i_right]:
                # p_len += 2
                i_left -= 1
                i_right += 1
            # return p_len, s[i_left + 1: i_right]
            return s[i_left + 1: i_right]
        
        longer_palindrome = lambda s1, s2: s1 if len(s1) > len(s2) else s2
            
        current_longest = ""
        middle = len(s) // 2
        i = middle
        n = 0
        # while -1 < i < len(s): # version with no early stop
        while -1 < i < len(s) and max_possible_lenght(i) > len(current_longest): # version with early stop
            odd_palindrome = palindrome(i, 1)
            even_palindrome = palindrome(i, 0)
            current_longest = longer_palindrome(odd_palindrome, even_palindrome)
            print(f"i: {i:<{len(str(len(s)))}} | odd: {odd_palindrome} | even: {even_palindrome} | longest: {current_longest}")
            # print(f"i: {i:<{len(str(len(s)))}} | odd: {odd_palindrome:<{len(s)}} | even: {even_palindrome:<{len(s)}} | longest: {current_longest}")
            n += 1
            i = middle + (-1)**(n + 1) * ((n + 1) // 2)

        return current_longest


# s = "babad"
# s = "babab"
# s = "abba"
# s = "abbcbba"
# s = "abbcbbax"
# s = "bbabbcbbax"
s = "bbabbcbbaxbbabbcbbax"
# s = "cbbd"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
