class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_tmp = str(x)
        reversed_result = ""
        if x < 0:
            for i in range(len(reversed_tmp) - 1, 0, -1):
                reversed_result = reversed_result + reversed_tmp[i]
            reversed_result = int(reversed_result)
            reversed_result = - reversed_result
        else:
            for i in range(len(reversed_tmp) - 1, -1, -1):
                reversed_result = reversed_result + reversed_tmp[i]
            reversed_result = int(reversed_result)
        x = reversed_result

        if abs(x) < 2 ** 31 and x != 2 ** 31 - 1:
            return x
        else:
            return 0


def result():
    s = Solution()
    nums = -123
    print(s.reverse(nums))


result()
