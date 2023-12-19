class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newArr = []
        for i in nums:
            if i != val:
                newArr.append(i)
                
        for i in range(len(newArr)):
            nums[i] = newArr[i]
            
        nums[:] = nums[:len(newArr)]
        
        return len(newArr)