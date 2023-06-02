# solution with high time complexity ~ O(n^3)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_string = len(s)
        if l_string == 0:
            return 0
        
        l_max = 1
        for l_substring in range(2, l_string + 1):
            for i in range(l_string - l_substring):
                print("checking: ", " " * i, s[i:i + l_substring + 1], " " * (l_string - l_substring - i),"l_max=", l_max)
                if len(list(s[i:i + l_substring])) == len(set(s[i:i + l_substring])):
                    l_max = l_substring
                    break
        return l_max
