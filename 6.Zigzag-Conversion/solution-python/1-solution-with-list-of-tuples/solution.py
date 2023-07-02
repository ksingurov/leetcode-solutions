class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x, y = 1, 1
        movements = {'down': [0, 1], 'up': [1, -1]}

        letters = [(s[0], x, y)]
        next_move = movements['down']
        for letter in s[1:]:
            x = x + next_move[0]
            y = y + next_move[1]
            letters += [(letter, x, y)]
            if y == numRows:
                next_move = movements['up']
            elif y == 1:
                next_move = movements['down']

        sorted_letters = sorted(letters, key=lambda x: (x[2], x[1]))
        zigzag = [letter[0] for letter in sorted_letters]
        return "".join(zigzag)
