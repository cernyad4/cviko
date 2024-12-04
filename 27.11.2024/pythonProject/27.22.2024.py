@calculate_time
def selection_sort(data):

    array = data.copy()
    size = len(array)

    for i in range(size):
        min_index = i

        for j in range(i, size):

            if array[j] < array[min_index]:
                min_index = j


        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

    return array

data = [7, 5, -19, 0, 9]
sorted_data = selection_sort(data)
print(f"Sorted array with selection sort: {sorted_data}")

@calculate_time
def bubble_sort(data):

    array = data.copy()
    size = len(array)

    for i in range(size):

        swapped = False

        for j in range(size - i - 1):

            if array[j] > array[j + 1]:

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True

            if not swapped:
                break

    return array

data = [7, 5, -19, 0, 9]
sorted_data = bubble_sort(data)
print(f"Sorted array with bubble sort: {sorted_data}")

def merge_sort(array):
    if len(array) > 1:

        half = len(array) // 2
        left = array[:half]
        right = array[half:]

        merge_sort(left)
        merge_sort(right)
        #print(f"left: {left}, right: {right}")
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

    return array

sorted_data = merge_sort(data)
print(f"Sorted array with merge sort: {sorted_data}")

import time
import random

array = []
for _ in range(10000):
    array.append(random.randint(-10000, 10000))

sorted_data = selestion_sort(array)
sorted_data2 = bubble_sort(array)

#nevim jak dál...