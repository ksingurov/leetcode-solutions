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

        for i, (inp, exp) in enumerate(test_data):
            with self.subTest(inp=inp, exp=exp):
                result = self.sol.longestPalindrome(inp)
                print(f" - SUBTEST {i+1}: input={inp}, expected={exp}, result={result}")
                if isinstance(exp, str):
                    self.assertEqual(result, exp)
                else:
                    self.assertIn(result, exp)

if __name__ == "__main__":
    unittest.main(verbosity=2)
