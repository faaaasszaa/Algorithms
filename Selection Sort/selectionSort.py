# Function to return the smallest index
def findSmallest(arr):
    # Starts at the first index of the array
    smallest = arr[0]
    # Createing a variable to store the index of the smallest element
    smallIndex = 0
    # Loops through the array based on its length
    for i in range(1, len(arr)):
        # If the current index is smaller than stored small index, we change values accordingy
        if arr[i] < smallest:
            smallest  = arr[i]
            smallIndex = i
    # We return the index of the smallest element
    return smallIndex

# Selection Sort Array (Runs on O(n^2))
def selectionSort(arr):
    # Creating an array to store from least go greatest
    newArr = []

    for i in range(0, len(arr)):
        smallElement = findSmallest(arr)
        # We find the smallest element then add it to the new array
        newArr.append(arr.pop(smallElement))
    return newArr

the_list = [7, 6, 3, 4, 6, 8, 9, 0, 1]

print("The index of the smallest element: " + str(findSmallest(the_list)))
print(selectionSort(the_list))




