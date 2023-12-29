class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Solution 1 68ms

        # length = len(nums)
        # ans = []
        # i = 0
        # j = 0
        # k = 0
        # while j < length*2:
        #     if j < length:
        #         ans.insert(j,nums[i])
        #         i += 1
        #     elif j >= length:
        #         ans.insert(j,nums[k])
        #         k += 1
        #     j += 1
        # return ans

        # Solution 2 57ms
        return nums*2

        # Solution 3 70ms
        # nums.extend(nums)
        # return nums