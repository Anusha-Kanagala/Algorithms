class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        if len(strs) == None:
            return list(strs)
        for word in strs:
            word_sorted = ''.join(sorted(word))
            if word_sorted in d:
                d[word_sorted] += [word]
            else:
                d[word_sorted] =[word]
        return d.values()


def driver():
    s= Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(strs))


driver()