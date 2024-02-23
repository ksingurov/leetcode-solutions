# 4.06.2025
# wrong answer, but the idea is correct
# instead of most common in the end we need to return the count of the maximum beauty

import collections
import itertools

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        # all f(x), i.e. number of times each character occurs in the string s
        occurances = collections.Counter(s) # dict {'character': occurance}

        # all possible subsequences of length k
        all_subsequences = itertools.combinations(list(s), k)
        # to get k-subsequences, keep only those with most common occurance equal to 1
        # element of k_subsequences is a list of characters
        k_subsequences = [sub for sub in all_subsequences if collections.Counter(sub).most_common(1)[0][1] == 1]

        # check if there are no subsequences
        if len(k_subsequences) == 0:
            return 0
        else:
            # list of all beauties of the string s
            beauties = []
            # for each k-subsequence calculate sum of occurances in the original string s
            # since elemenets in k_subsequences in a list, just list of occurances with list comprehensions, and the sum it
            for k_sub in k_subsequences:
                beauties += [sum([occurances[element] for element in k_sub])]

            # return the counter for most common element in the list of beauties
            return collections.Counter(beauties).most_common(1)[0][1]
    