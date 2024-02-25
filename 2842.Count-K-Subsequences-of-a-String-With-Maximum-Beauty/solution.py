import collections
import math

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        # all f(x), i.e. number of times each character occurs in the string s
        occurances = collections.Counter(s) # dict {'character': occurance}
        if len(occurances) < k:
            return 0

        # we need only k-subsequences which would have maximum possible beauty
        # i.e. those k-subsequences should contain unique charachters with biggest beaities, i.e. frequencies
        # thus let's find k most frequent chararters
        sorted_occurances = sorted(occurances.items(), key=lambda item: item[1], reverse=True)
        k_occurances = sorted_occurances[:k]

        # it is possible that several charachters might have the same frequency
        # it is not a problem if all of them among characters within first elements of sorted_occurances
        # however if k-th and k+1-th element have the same frequency
        # then there are several combinations of unique characters based on which we can compose k-subsequence
        kth_occurance = k_occurances[-1][1]
        n_kth_to_select = len([item for item in k_occurances if item[1] == kth_occurance])
        n_kth_total = len([item for item in sorted_occurances if item[1] == kth_occurance])

        # so now we just need to calculate number of combinations with k_occurances
        return math.prod([item[1] for item in k_occurances]) * math.comb(n_kth_total, n_kth_to_select)
