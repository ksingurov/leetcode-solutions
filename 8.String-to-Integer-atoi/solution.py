import re

class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r" *[+-]?\d+"
        s_lstrip = s.lstrip()
        match = re.match(pattern, s_lstrip)
        if match:
            return int(re.match(pattern, s_lstrip).group(0))
        return 0
        