class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1
        max_area = -1
        while low < high:
            curr_area = min(height[low], height[high]) * (high - low)
            if curr_area > max_area:
                max_area = curr_area

            if height[low] < height[high]:
                low = low + 1
            else:
                high = high - 1

        return max_area


def calc_area():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(height))


calc_area()
