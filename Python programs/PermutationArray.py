class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def permutSol(nums, temp):
            if not nums:
                res.append(temp[:])
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                ##print(nums[i+1:] + nums[:i])
                permutSol(nums[i + 1:] + nums[:i], temp)
                temp.pop()

        permutSol(nums, [])
        return res


def PermDriver():
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))


PermDriver()
