import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        # return super().setUp()
        self.sol = Solution()
    
    def test_case1(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcabcbb"), 3)
    
    def test_case2(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring("bbbbb"), 1)

    def test_case3(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring("pwwkew"), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
