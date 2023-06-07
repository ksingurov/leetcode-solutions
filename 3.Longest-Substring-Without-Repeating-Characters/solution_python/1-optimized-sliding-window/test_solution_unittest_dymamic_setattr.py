from solution import Solution
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

def create_test_function(input_string, expected_output):
    def test(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring(input_string), expected_output)
    return test

# test cases
test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
]

for i, (inp, exp) in enumerate(test_cases):
    test_name = f"test_case_{i}__input_{inp}__output_{exp}"
    test_func = create_test_function(inp, exp)
    setattr(TestSolution, test_name, test_func)

if __name__ == "__main__":
    unittest.main(verbosity=2)
