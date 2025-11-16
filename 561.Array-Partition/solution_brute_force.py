from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_mins = sum(nums[::2])
        return sum_mins
