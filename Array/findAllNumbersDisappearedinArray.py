class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        newList = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in newList:
                res.append(i)
        return res