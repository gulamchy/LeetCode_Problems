class BinarySearch:
    def binarySearch(self,arr,target):
        L, R = 0, len(arr)-1

        while L <= R:
            mid = (L+R) // 2

            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid -1
            else:
                return mid
        return -1

array = [1,2,3,4,5,6,7,8]
target = 5
search = BinarySearch()
result = search.binarySearch(array,target)

print(result)
