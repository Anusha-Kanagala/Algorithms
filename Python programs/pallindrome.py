class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        is_pallin = str(x)
        reverse_x = ""
        len_palin = len(is_pallin)
        ## reversing the string using a for loop
        """print(is_pallin[::-1])
        if x >= 0:
            for i in range(len(is_pallin)-1, -1, -1):
                reverse_x = reverse_x + is_pallin[i]
            if reverse_x == is_pallin:
                return True
            else:
                return False
        else:
            return False"""
        ##check if pallindrome using string slicing
        return x>=0 and is_pallin == is_pallin[::-1]


def is_Palindrome_check():
    s = Solution()
    x = 121
    print(s.isPalindrome(x))


is_Palindrome_check()
