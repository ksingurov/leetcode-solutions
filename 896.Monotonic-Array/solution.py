class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return (
            all([x >= y for x, y in zip(nums[:-1], nums[1:])]) \
            or all([x <= y for x, y in zip(nums[:-1], nums[1:])])
            )
