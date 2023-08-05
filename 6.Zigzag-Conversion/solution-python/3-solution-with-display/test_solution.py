from solution import Solution
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

def create_test(method, inp, exp):
    def test(self):
        # self.assertEqual(self.sol.convert(**inp), exp)
        self.assertEqual(getattr(self.sol, method)(**inp), exp)
    return test

test_data = {
    'convert': [
        ({'s': "PAYPALISHIRING", 'numRows': 3}, "PAHNAPLSIIGYIR"),
        ({'s': "PAYPALISHIRING", 'numRows': 4}, "PINALSIGYAHRPI"),
        ({'s': "A", 'numRows': 1}, "A")
    ],
    'display_zigzag': [
        ({'s': "PAYPALISHIRING", 'numRows': 3}, "P   A   H   N\nA P L S I I G\nY   I   R"),
        ({'s': "PAYPALISHIRING", 'numRows': 4}, "P     I     N\nA   L S   I G\nY A   H R\nP     I"),
        ({'s': "A", 'numRows': 1}, "A")
    ]
}

print("\n[SETTING UP]")
for method, cases in test_data.items():
    for i, (inp, exp) in enumerate(cases):
        # print(f"  test case: {i+1}")
        test_name = f"test_{method}__case_{i+1}"
        test_func = create_test(method, inp, exp)
        setattr(TestSolution, test_name, test_func)
    print(f"method: {method} ({len(cases)} cases)")

if __name__ == "__main__":
    print("\n[RUNNING TESTS]")
    unittest.main(verbosity=2)
