import collections

def finder(arr1,arr2):  #O(nlogn)

    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

def finder2(arr1,arr2):   #O(n) -> dictionary

    d = collections.defaultdict(int) #if key is not parent, adds it

    for num in arr2:
        d[num] += 1

    for num in arr1:

        if d[num] == 0:
            return num
        else:
            d[num] += 1

def finder3(arr1,arr2):

    result = 0

    for num in arr1+arr2:
        result ^= num
        print result

    return result



arr1 = [1,2,3,4]
arr2 = [1,2,3]

if __name__ ==  "__main__":

    # find 2 or more missing element

    a = [1, 3, 4, 5, 7, 8, 9, 10]
    b = [x for x in range(a[0], a[-1]+1)]
    print(b)
    a = set(a)
    print a
    print (list(a ^ set(b)))

#result = finder3(arr1,arr2)
#print(result)