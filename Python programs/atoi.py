class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        try:
            isNegative = False
            res = 0

            if s[0] == "-":
                isNegative = True

                s = s[1:]
            elif s[0] == "+":
                s = s[1:]

            i = 0
            while i < len(s) and s[i].isdigit():
                i += 1

            res = int(s[:i])
            if res != "":
                if isNegative == True:
                    if 0 - res < -2 ** 31:
                        return -2 ** 31
                    return 0 - res
                elif res >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                return res
            return 0
        except:
            return 0


def atoiDriver():
    s= Solution()
    s1 = "00000-42a1234"
    print(s.myAtoi(s1))


atoiDriver()