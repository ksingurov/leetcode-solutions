from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to letters on a phone keypad
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

        # Recursive function to generate combinations
        # Logic:
        # Input is a list of strings, and an index of the character (digit) to replace with letters
        # strings are supposed to be aplanumeric: left part before index are letters already chosen,
        # and right part after index are digits still present and to be replaced
        # The function generates all combinations for the given index
        # by replacing the digit at the index with letters from the phone_numbers mapping,
        # Then it recursively calls itself and passes the new combinations and the next index.
        def generate_combinations(combinmations, index=0):
            if index == len(combinmations[0]):
                return combinmations
            new_combinations = []
            for c in combinmations:
                new_combinations += [c[:index] + letter + c[index + 1:] for letter in phone_numbers[c[index]]]
            return generate_combinations(new_combinations, index + 1)

        # call the recursive function only if the input string is not empty
        if len(digits) > 0:
            return generate_combinations([digits])
        return []
