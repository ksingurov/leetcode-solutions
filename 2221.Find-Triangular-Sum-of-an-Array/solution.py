from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums_new = []
            for i in range(len(nums) - 1):
                nums_new += [(nums[i] + nums[i + 1]) % 10]
            return self.triangularSum(nums_new)
