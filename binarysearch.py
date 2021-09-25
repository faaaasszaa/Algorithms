def binary_search(list, item):
    # We establish the lower and upper boundaries of a sorted array
    low = 0
    high = len(list)-1

    while low <= high:

        # The algorithm starts by directly going to the middle of the array
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid

        # If the returned value is greater than the item, we shift the index
        # to the left part of the mid
        if guess > item:
            high = mid - 1

        # If the returned value is lower than the item,
        # we shift to the right of the mid
        else:
            low = mid + 1 

    # Returns -1 if an item is not in the given indewx
    return -1

the_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
59, 61, 67, 71, 73, 79, 83, 89, 97]

# Prints the index if there is one
n = int(input("Enter a number: "))
if binary_search(the_list, n) != -1:
    print("Item is present in index: " + str(binary_search(the_list, n)))
else:
    print("Item is not in the list!")
