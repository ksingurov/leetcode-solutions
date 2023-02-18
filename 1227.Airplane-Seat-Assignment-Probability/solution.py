class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n != 1:
            p1 = 1.0/n
            p21 = (n-2.0) / n
            p22 = self.nthPersonGetsNthSeat(n-1)
            return p1 + p21*p22
        else:
            return 1.0
