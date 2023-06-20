from solution import Solution

sol = Solution()

# base test cases from leetcode
assert sol.longestPalindrome("babad") in ("bab", "aba") 
assert sol.longestPalindrome("cbbd") == "bb"

# custom test cases
assert sol.longestPalindrome("babab") == "babab"
assert sol.longestPalindrome("abba") == "abba"
assert sol.longestPalindrome("abbcbba") == "abbcbba"
assert sol.longestPalindrome("bbabbcbbax") == "abbcbba"
assert sol.longestPalindrome("bbabbcbbaxbbabbcbbax") == "abbcbba"
