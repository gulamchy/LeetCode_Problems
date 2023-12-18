# from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # """
        # Do not return anything, modify arr in-place instead.
        # """
        # i = 0
        # while i < len(arr):
        #     if arr[i] == 0:
        #         arr.insert(i+1,0)
        #         arr.pop()
        #         i += 2
        #     else:
        #         i += 1
        
        newArr = []
        for n in arr:
            if n == 0:
                newArr.append(0)
            newArr.append(n)
        
        for i in range(len(arr)):
            arr[i] = newArr[i]