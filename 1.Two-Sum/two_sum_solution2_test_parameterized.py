import unittest
from parameterized import parameterized
from two_sum_solution2 import Solution

class TestTwoSumParameterized(unittest.TestCase):
    def setUp(self):
        self.solution = Solution() 

    @parameterized.expand([
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3], 7, []),  # Assuming no solution should return an empty list
    ])
    def test_two_sum(self, nums, target, expected):
        self.assertEqual(self.solution.twoSum(nums, target), expected)

if __name__ == '__main__':
    unittest.main() 