"""
My implementation of the bubble Sort algorithm

time complexity - O(n^2)
space complexity - O(1)

"""

def bubbleSort(array):
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(i , i+1 , array)
                isSorted = False

    return array

def swap(i,j , array):
    array[i] , array[j] = array[j] , array[i]