class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        notMatch = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                notMatch += 1
        return notMatch