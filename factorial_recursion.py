def fact(n):

    #base case
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print fact(5)

def rec_sum(n):

    #base case
    if n == 0:
        return 0

    else:

        return n + rec_sum(n-1)


def individual_sum(n):

    if len(n) == 1:
        return n

    else:

        return n%10 + individual_sum(n/10)

def word_split(phrase,list_of_words, output=None):

    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):

            output.append(word)

            return words_split(phrase[len(word):],list_of_words,output)

        return output
