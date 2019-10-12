# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Store the element in a temp variable
        temp = arr[i]
        # Swap the element found at the current index
        # with the next smallest element found
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Length of the array stops at the 2nd to the last element
    # because we will be comparing the current value to the next value each time
    len_of_arr = len(arr)-1
    # Loop through your array
    for i in range(len_of_arr):
        # Compare each element to its neighbor
        # by comparing the current j with the next value
        for j in range(len_of_arr - i):
            # if left element > right element
            if arr[j] > arr[j+1]:
                # swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
