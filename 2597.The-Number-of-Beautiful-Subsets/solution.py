import itertools
from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # there at least len(nums) beatifuls subsets, i.e. subsets of size 1
        beatiful_subsets_count = len(nums)

        # only subsets of size > 1
        subsets = []
        for subset_size in range(2, len(nums) + 1):
            subsets += [list(c) for c in itertools.combinations(nums, subset_size)]

        # check if any pair in the subset has a difference of k
        # if not, then it is a beatiful subset
        for subset in subsets:
            pairs = itertools.combinations(subset, 2)
            if any([abs(p[0] - p[1]) == k for p in pairs]):
                pass
            else:
                beatiful_subsets_count += 1

        return beatiful_subsets_count

