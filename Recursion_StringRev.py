def reverse(s):

    #Base

    if len(s) <= 1:
        return s

    # recursion

        return reverse(s[1:])+s[0]
    