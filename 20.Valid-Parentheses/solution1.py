import re

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        match = re.search(r"(\(\)|\[\]|\{\})", s)
        if match:
            return self.isValid(s[:match.span()[0]] + s[match.span()[1]:])
        return False
