
# to imporove performance, we check if the string s has at least k different characters
# and if not, return 0 immediately
# prevuois version of the code was checking len of k_subsequences

import collections
import itertools

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        # all f(x), i.e. number of times each character occurs in the string s
        occurances = collections.Counter(s) # dict {'character': occurance}

        # if there are less than k different characters in the string s, return 0
        # i.e. we cannot form a k-subsequence with unique characters
        if len(occurances) < k:
            return 0
        
        # all possible subsequences of length k
        all_subsequences = itertools.combinations(list(s), k)
        # to get k-subsequences, keep only those with most common occurance equal to 1
        # element of k_subsequences is a list of characters
        k_subsequences = [sub for sub in all_subsequences if collections.Counter(sub).most_common(1)[0][1] == 1]

        # list of all beauties of the string s
        beauties = []
        # for each k-subsequence calculate sum of occurances in the original string s
        # since elemenets in k_subsequences in a list, just list of occurances with list comprehensions, and the sum it
        for k_sub in k_subsequences:
            beauties += [sum([occurances[element] for element in k_sub])]

        # return the counter for biggest element in the list of beauties
        c = collections.Counter(beauties)
        m = max(c.keys())
        return c[m]
    