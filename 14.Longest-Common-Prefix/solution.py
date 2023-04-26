from typing import List
import collections

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = min([len(s) for s in strs])

        prefixes = ['']
        most_common_previous = 0
        for i in range(0, max_len):
            strs_to_check = [s[:i + 1] for s in strs if s[:i] in prefixes]
            count = collections.Counter(strs_to_check)
            most_common = count.most_common()[0][1]
            if most_common < most_common_previous or most_common == 1:
                break
            most_common_previous = most_common
            prefixes = [item[0] for item in count.items() if item[1] == most_common_previous]

        return prefixes[0]