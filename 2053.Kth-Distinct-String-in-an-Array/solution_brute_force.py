from collections import Counter
from typing import List

class Solution:
    from collections import Counter
    def kthDistinct(self, arr: List[str], k: int) -> str: #type: ignore
        count = Counter(arr)
        distincts = [k for k, v in count.items() if v == 1]
        if len(distincts) < k:
            return ""
        i = 0
        for a in arr:
            if a in distincts:
                i += 1
                if i == k:
                    return a
