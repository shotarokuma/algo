class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        first = matrix[0][0]
        last = matrix[-1][-1]
        if target < first or last < target:
            return False
        if target == first or target == last:
            return True
        if len(matrix) > 1:
            pivot = int(len(matrix) / 2)
            return self.searchMatrix(matrix[:pivot], target) or self.searchMatrix(matrix[pivot:], target)
        else:
            pivot = int(len(matrix[0]) / 2)
            return self.searchMatrix([matrix[0][:pivot]], target) or self.searchMatrix([matrix[0][pivot:]], target)