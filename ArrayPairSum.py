def pair_sum(arr,k):

    if len(arr)<2:
        return

    #sets for tracking

    seen = set()
    output = set()

    #pair_sum([1,3,2,2],4]
    for num in arr:

        target = k-num # 3 = 4-1 , 1 =4-3, 2=4-2, 2=4-2

        if target not in seen:
            seen.add(num)
            print(num)
        else:
            output.add( (min(num,target),max(num,target)) )


    print '\n'.join(map(str,list(output)))

arr = [1,3,2,2]
k=4
result = pair_sum(arr,k)
print(result)