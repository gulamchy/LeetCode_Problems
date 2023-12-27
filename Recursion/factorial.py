class Solution:
    def factorial(self, num: int) -> int:
        # recursion has higher space complexity
        if num <= 1:
            return 1
        return num * self.factorial(num-1)
        # use while loop to run the code in O(1) space complexity
        # res = 1
        # while num >1:
        #     res = res * 1
        #     num -= 1
        # return res

# s = Solution()
# p = s.factorial(5)
# print(p)