s = "abc"
t = "ahbgdc"

# is s a subsequence of t?
def isSubsequence(s, t):
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return i == len(s)


def su(s,t):
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
        
    return i == len(s)

print(su(s,t))