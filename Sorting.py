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

#-------------------------------------------------------------------------#

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

#-------------------------------------------------------------------------#

def insertionSort(arr):

    # n-1 passes to sort n items
    # order(n2)

    for i in range(1,len(arr)):

        current = arr[i]
        position = i

        while position > 0 and arr[position-1] > current:
            arr[position] = arr[position-1]
            position = position-1

        arr[position] = current


#-------------------------------------------------------------------------#


def shellSort(arr):

    # Shell-Sort improves on insertion sort by breaking the original list into a number of smaller sublists,
    # Uses i (gap) apart!
    # reduces the number of shifting operation of insertion sort
    # does small sort and then finally a insertion sort pass.
    sublistCount = len(arr)/2

    while sublistCount > 0:
        for start in range(sublistCount):
            gap_insertion_sort(arr,start,sublistCount)
            print(arr)
        sublistCount = sublistCount/2


def gap_insertion_sort(arr,start,gap):

    for i in range(start+gap,len(arr),gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentvalue:
            arr[position]= arr[position-gap]
            position = position - gap

        arr[position] = currentvalue


#-------------------------------------------------------------------------#

def quickSort(arr):

    # Quicksort select a value called pivot value
    # pivot assist with splitting the list and call recursively
    # does not use additional space

    return quickHelp(arr,0,len(arr)-1)



def quickHelp(arr,first,last):

    if first < last:

        splitPoint = partition(arr,first,last)

        quickHelp(arr,first,splitPoint-1)
        quickHelp(arr, splitPoint+1, last)

    return arr

def partition(arr,first,last):

    #returns the split point

    pivot = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark +=1
        while rightmark >= leftmark and arr[rightmark] >= pivot:
            rightmark -=1

        if rightmark < leftmark:
            done = True

        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

#-----------------------------------------------------------------------------#
def mergeSort(arr):

    # Merge Sort is a recursive algo that continually split a list in half.
    # split and recursively apply mergesort
    # atlast merge the sorted list.

    #while merge . if splits . Recursively
    if len(arr) > 1:

        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf [j]:
                arr[k] = lefthalf[i]
                i += 1

            else:

                arr[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr


#def heap_sort(arr):


arr = [1,367,8,90,899,53]
print arr
print quickSort(arr)

