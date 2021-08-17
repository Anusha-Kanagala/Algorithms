class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        dividend_n = abs(dividend)
        divisor_n = abs(divisor)
        result = 0
        while (dividend_n - divisor_n >= 0):
            count = 0

            while dividend_n - (divisor_n << 1 << count) >= 0:
                count = count + 1
            result = result + 1 << count
            dividend_n -= divisor_n << count

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            result = -result
        else:
            result = result

        return result


def divideDriver():
    s = Solution()
    dividend = 10
    divisor = 3
    print(s.divide(dividend, divisor))


divideDriver()
