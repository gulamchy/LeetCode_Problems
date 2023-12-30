class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        low, high = 0 , row * col - 1
        while low <= high:
            mid = (low+high) // 2
            if matrix[mid // col][mid % col] < target:
                low = mid + 1
            elif matrix[mid // col][mid % col] > target:
                high = mid - 1
            else: 
                return True
        return False


        # for m in matrix:
        #     for n in m:
        #         if n == target:
        #             return True
        # return False
