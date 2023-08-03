# to display zigzag we still need x coordinate
from typing import DefaultDict, Dict
from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = Solution.build_zigzag(s, numRows)
        return "".join([letter for line in zigzag.values() for letter in line.values()])

    @staticmethod
    def build_zigzag(s: str, numRows: int) -> DefaultDict[int, Dict[int, str]]:
        zigzag = defaultdict(dict)
        movements = {'down': (0, 1), 'up': (1, -1)}
        
        x, y = 1, 1
        next_move = movements['down']
        for letter in s:
            zigzag[y][x] = letter
            x += next_move[0]
            y += next_move[1]
            if y == numRows:
                next_move = movements['up']
            elif y == 1:
                next_move = movements['down']

        return zigzag



if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    res = sol.build_zigzag(s, numRows)
    print(res)
    res = sol.convert(s, numRows)
    print(res)
    # help(defaultdict)

    # row = 1
    # print(res[row])
    # # numCols = res[row][-1][0] #if zigzag = defaultdict(list)
    # numCols = max(res[row].keys())
    # # for i in range(1, numCols + 1):
    # #     print(res[row].get(i))
    # # print(numCols)
    # # line = [" " for i in range(numCols)]
    # # print(line)

    # # line = [res[row].get(i, " ") for i in range(1, numCols + 1)]
    # # print(" ".join(line))

    # lines = []
    # for row in range(1, numRows + 1):
    #     numCols = max(res[row].keys())
    #     line = " ".join([res[row].get(i, " ") for i in range(1, numCols + 1)])
    #     lines.append(line)
    
    # for line in lines:
    #     print(line)
