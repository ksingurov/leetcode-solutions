from collections import defaultdict

class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = Solution.build_zigzag(s, numRows)
        return "".join([letter for line in zigzag.values() for letter in line.values()])

    @staticmethod
    def display_zigzag(s: str, numRows: int) -> list[str]:
        if numRows == 1:
            return " ".join(list(s))
        zigzag = Solution.build_zigzag(s, numRows)
        lines = []
        for row in range(1, numRows + 1):
            numCols = max(zigzag[row].keys())
            line = " ".join([zigzag[row].get(i, " ") for i in range(1, numCols + 1)])
            lines.append(line)
        return "\n".join(lines) 

    @staticmethod
    def build_zigzag(s: str, numRows: int) -> defaultdict[int, dict[int, str]]:
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
    numRows = 4
    print(Solution.build_zigzag(s, numRows))
    print(Solution.convert(s, numRows))
    print(Solution.display_zigzag(s, numRows))
