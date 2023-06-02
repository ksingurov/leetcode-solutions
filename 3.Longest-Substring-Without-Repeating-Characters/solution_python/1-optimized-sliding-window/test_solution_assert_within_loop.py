from solution import Solution

test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
]

sol = Solution()
for s, expected in test_cases:
    assert sol.lengthOfLongestSubstring(s) == expected
