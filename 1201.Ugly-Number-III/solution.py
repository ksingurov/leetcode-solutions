class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        N = 0
        i = 0
        # while loop to check if number is is ugly
        while i < n:
            # in the beginning of the loop move to the next number to check
            N += 1
            # check if if candidate number is ugly
            if N % a == 0 or N % b == 0 or N % c == 0:
                # if ugly shift the counter
                i += 1
        return i
