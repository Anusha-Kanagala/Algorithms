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
            while (n != 0):
                result = result * (1 / x)
                n = n-1

        elif (n > 0):

            while (n != 0):
                result = result * x
                n = n - 1
        else:
            return result
        return result


def PowerDriver():
    s = Solution()
    x = 4
    n = 4
    print(s.myPow(x,n))


PowerDriver()
