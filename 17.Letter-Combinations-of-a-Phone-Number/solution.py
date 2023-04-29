from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_numbers = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def generate_combinations(combinmations, index=0):
            if index == len(combinmations[0]):
                return combinmations
            new_combinations = []
            for c in combinmations:
                new_combinations += [c[:index] + letter + c[index + 1:] for letter in phone_numbers[c[index]]]
            return generate_combinations(new_combinations, index + 1)

        if len(digits) > 0:
            return generate_combinations([digits])
        return []
