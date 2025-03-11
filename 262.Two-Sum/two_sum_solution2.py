# Problem: https://leetcode.com/problems/two-sum/
# Solution with O(n) time complexity and O(n) space complexity


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create an empty dictionary for number:index pairs
        dict_num_to_index = {}
        
        # Iterate over the list of numbers:
        for i, num1 in enumerate(nums):
            # What should be the second number, so that the sum of the two numbers is the target?
            num2 = target - num1
            # Check if such a number exists in the dictionary
            if num2 in dict_num_to_index:
                # If there is such a number, then we have found the pair of numbers, and can return the indices
                return [dict_num_to_index[num2], i]
            # Otherwise, add num1 and i to the dictionary
            dict_num_to_index[num1] = i
        # If loop is finished without returning, then no such pair is found and empty list is returned
        return []