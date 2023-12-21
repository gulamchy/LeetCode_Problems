class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #First Way
        # return max(list(set(nums))) if len(list(set(nums))) <3 else sorted(list(set(nums)))[-3]
        
        #Second Way
        newNums = list(set(nums))
        maximum= secondMax = thirdMax = float('-inf')
        
        if len(newNums) <= 2:
            return max(newNums)
        
        for i in newNums:
            if maximum < i:
                thirdMax = secondMax
                secondMax = maximum
                maximum = i
            elif secondMax < i:
                thirdMax = secondMax
                secondMax = i
            elif thirdMax < i:
                thirdMax = i
        return thirdMax