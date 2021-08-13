class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                      'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        if s in roman_dict.keys():
            return roman_dict[s]
        result = 0
        prev = s[0]
        result += roman_dict[prev]

        for i in s[1:]:
            curr = i
            if prev + curr in roman_dict.keys():
                result = result + roman_dict[prev + curr]- roman_dict[prev]
                prev = curr
            else:
                result = result + roman_dict[curr]
                prev = curr
        return result


def RomanToInt():
    s = Solution()
    nums = "MCMXCIV"
    print(s.romanToInt(nums))

RomanToInt()
