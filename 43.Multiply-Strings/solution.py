# The solution is based on so called "long multiplication" (or "column multiplication")
# https://en.wikipedia.org/wiki/Multiplication_algorithm#Long_multiplication

from itertools import product

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # create reversed lists of digits for input strings
        num1_digits = [int(d) for d in list(num1)[::-1]]
        num2_digits = [int(d) for d in list(num2)[::-1]]

        # multiply combinations of digits, also calculate power for corresponding product
        list_step1 = []
        for i, j in product(range(len(num1)), range(len(num2))):
            list_step1.append([num1_digits[i] * num2_digits[j], i + j])

        # calculate addens to sum
        list_step2 = [item[0] * pow(10, item[1]) for item in list_step1]

        # sum addens and convert result to string
        return str(sum(list_step2))
