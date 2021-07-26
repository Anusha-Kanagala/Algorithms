class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        one_count = nums.count(1)
        two_count = nums.count(2)
        low = 0
        for i in range(zero_count):
            nums[low] = 0
            low = low + 1
        for i in range(low,low+one_count):
            nums[low] = 1
            low = low + 1
        for i in range(low,low+two_count):
            nums[low] = 2
            low = low + 1


def sort_call():
    nums = [2, 0, 2, 1, 1, 0]
    s = Solution()
    s.sortColors(nums)

sort_call()
