class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subset = [[]]
        # for i in nums:
        #     subset += [curSet + [i] for curSet in subset]
        # return subset
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # Including item
            subset.append(nums[index])
            dfs(index + 1)

            # Excluding item
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return res