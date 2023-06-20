from solution import Solution
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # base test cases from leetcode
    def test_case1(self):
        self.assertIn(self.sol.longestPalindrome("babad"), ("bab", "aba"))

    def test_case2(self):
        self.assertEqual(self.sol.longestPalindrome("cbbd"), "bb")

    # custom test cases
    def test_case3(self):
        self.assertEqual(self.sol.longestPalindrome("babab"), "babab")
    
    def test_case4(self):
        self.assertEqual(self.sol.longestPalindrome("abba"), "abba")

    def test_case5(self):
        self.assertEqual(self.sol.longestPalindrome("abbcbba"), "abbcbba")

    def test_case6(self):
        self.assertEqual(self.sol.longestPalindrome("abbcbbax"), "abbcbba")

    def test_case7(self):
        self.assertEqual(self.sol.longestPalindrome("bbabbcbbax"), "abbcbba")

    def test_case8(self):
        self.assertEqual(self.sol.longestPalindrome("bbabbcbbaxbbabbcbbax"), "abbcbba")

if __name__ == "__main__":
    unittest.main(verbosity=2)
