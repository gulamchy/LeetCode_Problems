def merge(arr, start, mid, end):
    left = arr[start : mid+1] #mid+1 cause in python right value is not inclusive
    right = arr[mid+1 : end+1]

    i = 0 #index for left
    j = 0 #index for right
    k = start # index for array

    #merging two sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # adding remaining elements of one side
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    


def mergeSort(arr, start, end):
    if end - start+1 <= 1:
        return arr
    #middle of the array
    mid = (start+end) // 2

    #sort the left array
    mergeSort(arr,start,mid)

    #sort right array
    mergeSort(arr, mid, end)

    #merge sorted half
    merge(arr, start, mid, end)

    return arr