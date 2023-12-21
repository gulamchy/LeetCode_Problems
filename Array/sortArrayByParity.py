class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        evenArr = []
        
        for i in range(length):
            if nums[i] % 2 == 0:
                evenArr.append(nums[i])
                nums[i] = 0
        
        nums.sort()
        
        for i in range(len(evenArr)):
            if nums[i] == 0:
                nums[i] = evenArr[i]
            
        return nums