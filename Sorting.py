import sys
# www.sorting-algorithms.com
# www.visualgo.net

def swap(A,x,y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def BubbleSort(arr):

    # n-2 pairs
    # multiple pass
    # 1st pass will place the max at end of the list(n-1 place)
    # 2nd pass will place the second max at the n-2 place and so on.
    # Worst,Best,avg case- O(n2)

    # from n-1 to 0 in steps of -1
        nums = list(arr)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if arr[j] < arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
        return arr

def SelectionSort(arr):

    #improves on the bubble sort
    #takes the largest element in the list and place in nth position for the first pass
    #takes the second largest element in the list and places it in n-2 for the second pass and so on.
    # can be smallest or largest element.

    for slot in range(len(arr)-1,0,-1):

        MaxPosition = 0
        for loc in range(1,slot+1):
            if arr[loc] > arr[MaxPosition]:
                MaxPosition = loc
        temp = arr[slot]
        arr[slot] = arr[MaxPosition]
        arr[MaxPosition] = temp

    return arr
#def quick_sort(arr):

#def merge_sort(arr):

#def heap_sort(arr):


arr = [1,367,8,90,899,53]
print arr
#print BubbleSort(arr)
print SelectionSort(arr)

