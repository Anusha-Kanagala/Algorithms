class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = ""
        if len(strs) == 0:
            return LCP
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(LCP + i):
                LCP += i
            else:
                break
        return LCP


def LCP():
    s = Solution()
    strs = ["aaa","aa","aaa"]
    print(s.longestCommonPrefix(strs))


LCP()
