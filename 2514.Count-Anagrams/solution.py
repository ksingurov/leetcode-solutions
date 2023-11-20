import itertools
import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split()
        if len(words) == 1:
            other_words = set([''.join(p) for p in itertools.permutations(words[0])])
            return len(other_words)
        else:
            return math.prod(self.countAnagrams(word) for word in words)
