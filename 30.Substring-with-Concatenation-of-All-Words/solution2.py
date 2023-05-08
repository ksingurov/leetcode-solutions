# More efficient solution
# This solution finds all occurrences of each word in the string and checks for valid sequences

from typing import List
from itertools import permutations, product
from re import finditer

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        occurrences = []
        for w in words:
            matches = [match.start() for match in finditer(w, s)]
            if len(matches) == 0:
                return []
            occurrences.append(matches)

        n = len(words)
        l = len(words[0])
        sequences = []
        for perm in permutations(occurrences):
            sequences.extend(product(*perm))

        return list({c[0] for c in sequences if all(c[i + 1] - c[i] == l for i in range(n - 1))})
