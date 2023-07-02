# compose description

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def max_possible_lenght(i):
            return 2 * (len(s) - i) - 1

        def palindrome(i, parity):
            i_left = i - parity
            i_right = i + 1
            while i_left > -1 and i_right < len(s) and s[i_left] == s[i_right]:
                i_left -= 1
                i_right += 1
            return s[i_left + 1: i_right]
        
        def longer_palindrome(s1, s2):
            return s1 if len(s1) > len(s2) else s2
            
        current_longest = ""
        middle = (len(s) - 1) // 2
        i = middle
        n = 0
        while -1 < i < len(s) and max_possible_lenght(i) > len(current_longest):
            odd_palindrome = palindrome(i, 1)
            even_palindrome = palindrome(i, 0)
            new_longest = longer_palindrome(odd_palindrome, even_palindrome)
            current_longest = longer_palindrome(current_longest, new_longest)
            # print(f"i: {i} | odd: {odd_palindrome} | even: {even_palindrome} | longest: {current_longest}")
            n += 1
            i = middle + (-1)**(n + 1) * ((n + 1) // 2)

        return current_longest
