def compress(s):

    r = ""                          # result string
    l = len(s)

    if l == 0:                      #if length is 0 return, if length is 1 return the character with count 1
        return
    if l == 1:
        return s+"1"

    last = s[0]                     # to keep track , not necessary
    count = 1
    i = 1

    while i < l:

        if s[i] == s[i-1]:          #if the current letter and previous letter are same, increment count
            count +=1
        else:                           #else if concatenate the result string, previous string with the count
            r = r + s[i-1] + str(count)
            count = 1                   #reset the count value to 1
        i+=1                              #increment the i value
    r = r + s[i-1] + str(count)      #   concatenate the result string,previous string with count

    return r

s = "aaAABBBBCCC"
print compress(s)
