from solution import Solution
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

def create_test_function(inp, expected):
    if isinstance(expected, str):
        def test(self):
            self.assertEqual(self.sol.longestPalindrome(inp), expected)
    else:
        def test(self):
            self.assertIn(self.sol.longestPalindrome(inp), expected)
    return test

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
    if isinstance(exp, str):
        test_name = f"test_case_{i+1}__input_{inp}__output_{exp}"
    else:
        exp_str = "_".join(exp)
        test_name = f"test_case_{i+1}__input_{inp}__output_{exp_str}"
    test_func = create_test_function(inp, exp)
    setattr(TestSolution, test_name, test_func)

if __name__ == "__main__":
    unittest.main(verbosity=2)
