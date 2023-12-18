class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        start = 0
        for i in range(len(pref)):
            arr.append(pref[i]^start)
            start = pref[i]
        return arr