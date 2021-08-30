class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        temp = ""
        count = 0
        if s.isalpha():
            return 0
        for i in s:
            if i == " " or i == 0:
                count = count + 1
                pass
            if i == '+':
                result = result
                count = count + 1
                pass
            elif i == '-':
                result = -result
                count = count + 1
                pass

            while (count < len(s)):
                temp = temp + s[count]
                count = count + 1

            if -2 ** 31 <= int(temp) <= 2 ** 31:
                result = temp

            else:
                return 0
        return result


def atoiDriver():
    s= Solution()
    s1 = "42"
    print(s.myAtoi(s1))


atoiDriver()