class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        result = list([])
        if len(matrix) == 1:
            return matrix
        temp_result = []
        matrix_transpose = zip(*matrix)
        for i in matrix_transpose:
            for k in reversed(i):
                if len(temp_result) > len(matrix[0])-1:
                    result.append(temp_result)
                    temp_result = []
                temp_result = temp_result + [k]
        result.append(temp_result)
        return result


def imageDriver():
    s = Solution()
    #matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(s.rotate(matrix))


imageDriver()

