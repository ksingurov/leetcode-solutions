# use defaultdict instead of list of typles
# in this case it is appended in a "right" order while looping over input string
# actually we don't need x coordinate since letters are already ordered in rows accordingly

from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = defaultdict(list)
        y = 1
        next_move = 1
        for letter in s:
            zigzag[y].append(letter)
            y += next_move
            if y == numRows:
                next_move = -1
            elif y == 1:
                next_move = 1

        return "".join([item for v in zigzag.values() for item in v])
