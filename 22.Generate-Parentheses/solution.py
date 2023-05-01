# Solition based on recursion and backtracking
# Logic:
# 1. Start with list containing an empty string.
# 2. Recursively generate combinations by adding '(' or ')' based on:
# - the difference of counts of left and right parentheses
# - and, length of the current combinations
# Combinations are generated until they reach the length of 2 * n.

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(combinations):
            if len(combinations[0]) == 2 * n:
                return combinations
            new_combinations = []
            for c in combinations:
                open_count = c.count("(") - c.count(")")
                if open_count == 0:
                    new_combinations.append(c + "(")
                elif open_count == n or len(c) > n:
                    new_combinations.append(c + ")")
                else:
                    new_combinations.extend([c + "(", c + ")"])
            return generate(new_combinations)

        return generate([""])
