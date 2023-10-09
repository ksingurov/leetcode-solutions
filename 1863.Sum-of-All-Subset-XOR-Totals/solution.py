import itertools
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def XOR_list(lst):
            result = 0
            for i in lst:
                result ^= i
            return result

        sum = 0
        for subset_size in range(len(nums) + 1):
            for subset in itertools.combinations(nums, subset_size):
                sum += XOR_list(subset)
        return sum
