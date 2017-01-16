def fibo_iter(n):

    #a=0 and b=1
    #use tuple unpacking
    a,b=0,1

    for i in range(n):

        #tuple unpacking method in python
        # a=b,b=a+b
        a,b = b,a+b

    return a

def fibo_rec(n):

    #base case
    if n == 0 or n == 1:
        return n

    #recursive case
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

# memoization : storing stuffs of previous results in the memory

n = 10
cache = [None]*(n+1)

def fib_dynamic(n):

    #base case
    if n == 0 or n == 1:
        return n

    #check cache
    if cache[n] != None:
        return cache[n]

    #keep setting cache
    #helps to keep track of previous value, improves efficiency
    cache[n] = fib_dynamic(n-1) + fib_dynamic(n-2)

    return cache[n]


    #keep setting cache

