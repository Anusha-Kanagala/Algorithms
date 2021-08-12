class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                      'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        def get_key(val):
            for key, value in roman_dict.items():
                if val == value:
                    return key
        values = sorted(list(roman_dict.values()), reverse=True)
        print(values)
        result = ""

        while num != 0:

            # Find biggest value smaller or equal to num
            for val in values:
                if val <= num:
                    break

            result = result + get_key(val)
            num -= val

        return result


def IntToRoman():
    s = Solution()
    nums = 58
    print(s.intToRoman(nums))

IntToRoman()
