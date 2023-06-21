from solution import Solution
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()


    def test_cases(self):
        test_data = [
        # base test cases from leetcode
            ("babad", ("bab", "aba") ),
            ("cbbd", "bb"),
        # custom test cases
            ("babab", "babab"),
            ("abba", "abba"),
            ("abbcbba", "abbcbba"),
            ("abbcbbax", "abbcbba"),
            ("bbabbcbbax", "abbcbba"),
            ("bbabbcbbaxbbabbcbbax", "abbcbba")
        ]

        for inp, exp in test_data:
            with self.subTest(inp=inp, exp=exp):
                if isinstance(exp, str):
                    self.assertEqual(self.sol.longestPalindrome(inp), exp)
                else:
                    self.assertIn(self.sol.longestPalindrome(inp), exp)

if __name__ == "__main__":
    unittest.main()
