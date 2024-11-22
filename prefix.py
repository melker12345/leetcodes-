# Longest prefix

strs = ["dog", "docecar", "docar"]

def f(strs):
    # handle no input
    if not strs:
        return ""    

    # loops through the lenght of the first element on the array strs  
    for i in range(len(strs[0])):
        # create a place holder that holds the character that will be checked against the other strings 
        char = strs[0][i]
        # loop through all the strings in the strs array 
        for s in strs[1:]:
            # check if the elements in the first string is == to the len of the other strings OR if the elements of the other strings is != to the char  
            if i == len(s) or s[i] != char:
                # returns the characters that matches in all the strings 
                return strs[0][:i]
    # here we return the first index of the strs array why?  
    return strs[0]


def s(strs):
    if not strs:
        return ''

    for i in range(len(strs[0])):
        char = strs[0][i]

        for j in strs[i:]:
            if i == len(j) or j[i] != char:
                return strs[0][:i]
            
    return strs[0]



print(s(strs))
