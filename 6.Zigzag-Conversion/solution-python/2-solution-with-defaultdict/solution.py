# use defaultdict instead of list of typles
# in this case it is appended in a "right" order while looping over input string

from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = defaultdict(list)
        movements = {'down': (0, 1), 'up': (1, -1)}
        
        x, y = 1, 1
        next_move = movements['down']
        for letter in s:
            zigzag[y].append((x, letter))
            x = x + next_move[0]
            y = y + next_move[1]
            if y == numRows:
                next_move = movements['up']
            elif y == 1:
                next_move = movements['down']

        new_string = "".join([item[1] for v in zigzag.values() for item in v])
        return new_string

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    exp = "PAHNAPLSIIGYIR"
    sol = Solution()
    res = sol.convert(s=s, numRows=numRows)
    print(res == exp)
    # print(res)
    # help(defaultdict)
