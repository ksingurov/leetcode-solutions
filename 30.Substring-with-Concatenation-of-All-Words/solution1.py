# Brute force solution to find all permutations of words and check their presence in the string

from typing import List
from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        perms  = set(permutations(words, len(words)))
        concantenated_strings = set([''.join(p) for p in perms])

        indices = set()
        for c in concantenated_strings:
            index = s.find(c)
            if index != -1:
                indices.add(index)

        return list(indices)
