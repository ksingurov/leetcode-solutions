# a bit less brute force solution

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(min(limit, n) + 1):
            for j in range(max(0, n - i - limit), min(limit, n - i) + 1):
                # print("1st: ", i , "\t2nd: ", j, "\t3rd: ", n - i - j)
                count += 1
        return count