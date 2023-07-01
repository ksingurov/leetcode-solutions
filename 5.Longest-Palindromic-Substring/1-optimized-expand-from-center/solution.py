# version which returns lenght of longest palindrome, we need a palindrome itself

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def max_possible_lenght(i):
            return 2 * (len(s) - i) - 1


s = "babad"
# s = "babab"
# s = "abba"
# s = "abbcbba"
# s = "abbcbbax"
# s = "bbabbcbbax"
# s = "cbbd"


def max_possible_lenght(i):
            return 2 * (len(s) - i) - 1

for i in range(len(s)):
    # res = max_possible_len(i % 2, i) # v2
    res = max_possible_lenght(i)
    print(res)
