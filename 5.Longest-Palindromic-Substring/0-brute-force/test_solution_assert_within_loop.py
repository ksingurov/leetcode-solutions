from solution import Solution

test_cases = [
# base test cases from leetcode
    ("babad", ("bab", "aba") ),
    ("cbbd", ("bb")),
# custom test cases
    ("babab", ("babab")),
    ("abba", ("abba")),
    ("abbcbba", ("abbcbba")),
    ("abbcbbax", ("abbcbba")),
    ("bbabbcbbax", ("abbcbba")),
    ("bbabbcbbaxbbabbcbbax", ("abbcbba"))
]

sol = Solution()
for inp, exp in test_cases:
    assert sol.longestPalindrome(inp) in exp
