def findSmallest(arr):
    smallest = arr[0]
    smallIndex = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest  = arr[i]
            smallIndex = i
        return smallIndex

def selectionSort(arr):
    sorted_array = []

    for i in range(1, len(arr)):
        smallElement = findSmallest(arr)
        sorted_array.append(arr.pop(smallElement))
    return sorted_array

the_list = [3, 2, 6, 8, 9, 1, 10, 13, 12]

print(findSmallest(the_list))
print(selectionSort(the_list))




