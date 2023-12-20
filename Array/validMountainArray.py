class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        peakIndex = arr.index(max(arr))
        
        if length < 3:
            return False
        if peakIndex == 0 or peakIndex == length -1:
            return False
        
        for i in range(peakIndex):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(peakIndex,length-1):
            if arr[i] <= arr[i+1]:
                return False
            
        return True