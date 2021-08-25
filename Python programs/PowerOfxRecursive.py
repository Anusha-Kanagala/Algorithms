class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1

        if (n < 0):
            n = abs(n)
            x = 1 / x
        if (n % 2 == 0 and n != 0):
            temp_sol = self.myPow(x, n // 2)
            result = temp_sol * temp_sol
        elif (n != 0):
            temp_sol = self.myPow(x, n // 2)
            result = temp_sol * temp_sol * x
        return result