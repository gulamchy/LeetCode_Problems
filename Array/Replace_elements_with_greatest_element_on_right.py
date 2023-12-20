class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lastValue = -1
        for i in range(len(arr)-1,-1,-1):
            cur = arr[i]
            arr[i] = lastValue
            lastValue = max(lastValue,cur)
        return arr