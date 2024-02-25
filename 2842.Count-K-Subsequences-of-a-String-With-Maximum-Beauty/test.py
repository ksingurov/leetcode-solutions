import collections
import math

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        # all f(x), i.e. number of times each character occurs in the string s
        occurances = collections.Counter(s) # dict {'character': occurance}
        # print(occurances)
        if len(occurances) < k:
            return 0

        # we need only k-subsequences which would have maximum possible beauty
        # i.e. those k-subsequences should contain unique charachters with biggest beaities, i.e. frequencies
        # thus let's find k most frequent chararters
        sorted_occurances = sorted(occurances.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_occurances)

        k_occurances = sorted_occurances[:k]
        # print(k_occurances)
        kth_occurance = k_occurances[-1][1]  # the k-th most frequent character's frequency
        # print(kth_occurance)

        n_kth_to_select = len([item for item in k_occurances if item[1] == kth_occurance])
        n_kth_total = len([item for item in sorted_occurances if item[1] == kth_occurance])
        # print(n_kth_to_select, n_kth_total)

        return math.prod([item[1] for item in k_occurances]) \
                * math.comb(n_kth_total, n_kth_to_select)
        # return 0
    
# s = "aaabbc"
# k = 2

# s = "abbccd"
# k = 3

s = "abbcd"
k = 4

# s = "aabbccdd"
# k = 2

sol = Solution()
print(sol.countKSubsequencesWithMaxBeauty(s, k))
