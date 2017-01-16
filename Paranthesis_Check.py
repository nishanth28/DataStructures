def balanced_check(s):

    # scan string from right to left , push open paranthesis into the stack , pop when close paranthesis

    #edge case

    if len(s)%2 != 0:
        return False

    open = set('([{')

    pairs = set([('(',')'),('{','}'),('[',']')])

    stack = []

    for par in s:               #scanning from left to right

        if par in open:         #everytime we see a opening paranthesis, we push it to the stack.
            stack.append(par)   #stack is a list data structure
                                #we do this as we want the last opening paranthesis to be closed first
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()  # to find the match of the last opened paranthesis, we pop it

            if (last_open,par) not in pairs:
                return False

    return len(stack) == 0


s = "{((({})))}"
print balanced_check(s)
