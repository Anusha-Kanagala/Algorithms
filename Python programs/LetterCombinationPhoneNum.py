from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_dict = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
                       '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8':
                           ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        tup_list = []

        if len(digits) == 0:
            return []

        for i in product(*(letter_dict[d] for d in digits if d in letter_dict)):
            tup_list.append(''.join(i))
        return tup_list


def letter_driver():
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))


letter_driver()
