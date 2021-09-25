def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        print(mid)
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1 
    return False

the_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
59, 61, 67, 71, 73, 79, 83, 89, 97]
n = 11

if binary_search(the_list, n) != False:
    print("Item is in index: " + str(binary_search(the_list, n)))
else:
    print("Item is not in the list!")
