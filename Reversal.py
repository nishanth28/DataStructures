def StringRev(s):

    result = s[::-1]  #slicing : [start:Begin:step]
    return result

def reverse_string(string):

    new_strings = []
    index = len(string)
    while index:                #reverse a string using while loop
        index -= 1
        new_strings.append(string[index])
    return ''.join(new_strings)

def sentenceRev(s):

    words = []
    index = len(s)
    space = [' ']

    i = 0

    while i < index:

        if s[i] not in space:                             # if not a space Word_begin at that index

            word_begin = i

            while i < index and s[i] not in space:          #if not a space and i is lesser than index,increment i

                i+=1

            words.append(s[word_begin:i])                   #append the word from begin and till the end.

        i+=1                                                #finds the space, increments by 1

    return " ".join(reversed(words))







s = "nishanth is good"
res = sentenceRev(s)
print(res)
