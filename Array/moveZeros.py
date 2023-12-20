class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newArr = []
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                newArr.append(nums[i])
            j += 1
        diff = len(nums) - len(newArr)
        for i in range(diff):
            newArr.append(0)
        nums[:] = newArr[:]