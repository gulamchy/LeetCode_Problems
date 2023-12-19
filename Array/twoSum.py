from typing import List
# Remove top import when using in leetCode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0,length):
            for j in range(i+1,length):
                if (nums[i]+nums[j])==target:
                    return [i,j]

#sample input - try it when you are running the code in local.
# nums = [2, 7, 11, 15]
# target = 9

# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)