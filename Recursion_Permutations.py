# itertools

#iterate through "abcd"
#iterate through the initial string
#if we iterate through b . find all combination of acd
#once you have the element of n-1 permuations. add b to the final list

def permute(s):

    out = []

    #Base case
    if len(s) == 1:
        out = [s]

    else:

        # for every letter in string

        for i,letter in enumerate(s):

            #for every permuating resultiing from step 2 and 3

            for perm in permute(s[:i] + s[i+1:]):

                print "currentletter:"+letter
                print "permuation using rec:"+perm

                out += [letter+perm]

    return out

print permute("1234")