class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) > 2:
            for i in range(len(nums)-2):
                for j in range(i+1, len(nums)-1):
                    if nums[i] + nums[i+1] == nums[j] + nums[j+1]:
                        return True
        return False
