class Solution(object):
    def isPalindrome(self, s):
        l = len(s)
        left = s[:l//2]
        right = s[l:(l+1) // 2 - 1:-1]
        return left == right

    def shortestPalindrome(self, s):
        l = len(s)
        if l == 0:
            return s
        for i in range(l):
            if self.isPalindrome(s[:l-i]):
                return s[l:l-i-1:-1] + s
