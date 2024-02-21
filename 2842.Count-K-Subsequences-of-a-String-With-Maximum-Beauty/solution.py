import collections
import itertools

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        occurances = collections.Counter(s)

        k_subsequences = itertools.combinations(list(s), k)
        # TODO: filter out subsequences with different characters

        beauties = []
        for k_sub in k_subsequences:
            beauties += [sum([occurances[element] for element in k_sub])]

        return collections.Counter(beauties).most_common(1)[0][1]

        