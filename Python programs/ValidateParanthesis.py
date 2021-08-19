class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            if '()' in s:
                s = s.replace('()', '')
            elif '{}' in s:
                s = s.replace('{}', '')
            elif '[]' in s:
                s = s.replace('[]', '')

            else:
                return not s



def validateParenDriver():
    s= Solution()
    s1 = "{[])"
    s.isValid(s1)


validateParenDriver()
