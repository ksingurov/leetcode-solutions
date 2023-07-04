from solution import Solution
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

def create_test_function(inp, exp):
    s = inp[0]
    numRows = inp[1]
    def test(self):
        self.assertEqual(self.sol.convert(s, numRows), exp)
    return test

test_data = [
    (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
    (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
    (("A", 1), "A")
]

for i, (inp, exp) in enumerate(test_data):
    inp_str = "_".join([str(item) for item in inp])
    test_name = f"test_case_{i+1}__input_{inp_str}__output_{exp}"
    test_func = create_test_function(inp, exp)
    setattr(TestSolution, test_name, test_func)

if __name__ == "__main__":
    unittest.main(verbosity=2)
