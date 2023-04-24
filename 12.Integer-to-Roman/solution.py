class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        places = [int(n) for n in reversed(list(str(num)))]

        for i in range(1, len(places) + 1):
            place = places[i - 1]
            print(i, place)
            if i == 1:
                if place == 0:
                    roman += ['']
                elif place < 4:
                    roman += ['I' * place]
                elif place == 4:
                    roman += ['IV']
                elif place < 9:
                    roman += ['V' + 'I' * (place - 5)]
                else:
                    roman += ['IX']
            if i == 2:
                if place == 0:
                    roman += ['']
                elif place < 4:
                    roman += ['X' * place]
                elif place == 4:
                    roman += ['XL']
                elif place < 9:
                    roman += ['L' + 'X' * (place - 5)]
                else:
                    roman += ['XC']
            if i == 3:
                if place == 0:
                    roman += ['']
                elif place < 4:
                    roman += ['C' * place]
                elif place == 4:
                    roman += ['CD']
                elif place < 9:
                    roman += ['D' + 'C' * (place - 5)]
                else:
                    roman += ['CM']
            if i == 4:
                roman += ['M' * place]

        return "".join(reversed(roman))
