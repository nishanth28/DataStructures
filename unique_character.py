def unique_char(s):
    return  len(set(s)) == len(s)   #set takes all the unique characters in a string

s = "abe"
print unique_char(s)


def unique_char(s):
    char = set()

    for let in s:
        if let in char:
            return False
        else:
            char.add(let)

    return True