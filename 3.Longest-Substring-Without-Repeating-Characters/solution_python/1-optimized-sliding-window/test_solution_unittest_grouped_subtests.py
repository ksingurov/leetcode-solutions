import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        # return super().setUp()
        self.sol = Solution()
    
    def test_cases(self):
        test_data = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3)
        ]
        for s, expected in test_data:
            with self.subTest(s=s):
                self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main()
