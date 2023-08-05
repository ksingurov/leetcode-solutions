from collections import defaultdict

class Solution:
    def __init__(self):
        self.s = None
        self.numRows = None
        self.zigzag = None
        self.converted_string = None
        self.display_string = None

    def convert(self, s: str, numRows: int) -> str:
        self.s = s
        self.numRows = numRows
        self.zigzag = self.__build_zigzag()
        self.converted_string = "".join([letter for line in self.zigzag.values() for letter in line.values()])
        return self.converted_string

    def display_zigzag(self, s: str, numRows: int) -> list[str]:
        self.s = s
        self.numRows = numRows
        self.zigzag = self.__build_zigzag()
        lines = []
        for row in range(1, numRows + 1):
            numCols = max(self.zigzag[row].keys())
            line = " ".join([self.zigzag[row].get(i, " ") for i in range(1, numCols + 1)])
            lines.append(line)
        self.display_string = "\n".join(lines)
        return self.display_string 

    def __build_zigzag(self) -> defaultdict[int, dict[int, str]]:
        zigzag = defaultdict(dict)
        movements = {'down': (0, 1), 'up': (1, -1)}
        x, y = 1, 1
        next_move = movements['down']
        for letter in self.s:
            zigzag[y][x] = letter
            x += next_move[0]
            y += next_move[1]
            if y == self.numRows:
                next_move = movements['up']
            elif y == 1:
                next_move = movements['down']
        return zigzag


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    # res1 = sol.build_zigzag(s, numRows)
    # res1 = sol.build_zigzag()
    # print(res1)
    res2 = sol.convert(s, numRows)
    print(res2)
    res3 = sol.display_zigzag(s, numRows)
    print(res3)
