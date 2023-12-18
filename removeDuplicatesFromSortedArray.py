class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newArr =[nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                newArr.append(nums[i])
        
        for i in range(len(newArr)):
            nums[i] = newArr[i]
        
        nums[:] = nums[:len(newArr)]
        
        return len(nums)