class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        result = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                result = i
                break
        return result
