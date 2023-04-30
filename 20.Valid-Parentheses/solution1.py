# Elegant solution with recursion and regex.
# Logic:
# Recursively remove pairs of valid parentheses, brackets, or braces from the string.
# If the string becomes empty, it means all pairs were valid, and we return True.
# If no pairs can be removed and the string is not empty, we return False.

import re

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        match = re.search(r"(\(\)|\[\]|\{\})", s)
        if match:
            return self.isValid(s[:match.span()[0]] + s[match.span()[1]:])
        return False
