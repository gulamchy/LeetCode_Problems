class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i<len(nums1):
            if i == m:
                nums1.insert(i,nums2[j])
                nums1.pop()
                m += 1
                j += 1
            i += 1
        nums1 = nums1.sort()