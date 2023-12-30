# class ArrayReader:
#     def __init__(self, arr):
#         self.arr = arr

#     def get(self, index):
#         if 0 <= index < len(self.arr):
#             return self.arr[index]
#         else:
#             return -1

def search(self, reader, target):
        # Find the bounds of the array
    left, right = 0, 1

    while reader.get(right) < target and reader.get(right) != -1:
        left = right
        right *= 2

        # Perform binary search within the identified bounds
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = reader.get(mid)

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target and mid_val != -1:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found