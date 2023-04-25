class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        symbols = list(s)

        res = 0
        for i in range(len(symbols) - 1):
            if roman_to_int_dict[symbols[i]] >= roman_to_int_dict[symbols[i + 1]]:
                res += roman_to_int_dict[symbols[i]]
            else:
                res -= roman_to_int_dict[symbols[i]]
        res += roman_to_int_dict[symbols[-1]]
        
        return res
        