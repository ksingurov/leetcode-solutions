class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        unique_nums = set(nums)
        d = {}
        for n in unique_nums:
            d[n] = len([i for i in nums if i == n])
        d = sorted(d.items(), key=lambda elem: elem[1], reverse=True)[:k]
        return [i[0] for i in d]
