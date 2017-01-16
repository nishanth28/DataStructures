import re


def un_camel(x):

    final = ''                          # empty final string
    for item in x:
        if item.isupper():              #if caps
            final += "_"+item.lower()   #add _ and change to lower case
        else:
            final += item               #add the normal item.
    if final[0] == "_":                 #if first element is _, replace from string of 1st position
        final = final[1:]
    return final

#def camel_Re(x):



result = un_camel("nishanthPannerslvam")
print(result)