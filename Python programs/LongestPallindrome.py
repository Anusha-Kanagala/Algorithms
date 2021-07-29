class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_old = ""
        result_new = ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if s[i:j] == s[i:j][::-1]:
                    result_new = s[i:j]
                    if len(result_old) < len(result_new):
                        result_old = result_new
                        break
        return result_old



def longest_pallin():
    s = Solution()
    pallin_str = "dabab"
    print(s.longestPalindrome(pallin_str))


longest_pallin()
