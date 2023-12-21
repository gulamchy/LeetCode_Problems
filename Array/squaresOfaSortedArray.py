class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaresList = []
        numsLength = len(nums)
        for i in range(0,numsLength):
            squares = nums[i] * nums[i]
            squaresList.append(squares)
        return sorted(squaresList)