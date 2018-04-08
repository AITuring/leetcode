
def findTheDifference(s, t):

    """
    :type s: str
    :type t: str
    :rtype: str
    """
    a=list(t)
    for i in s:
        if i  in t:
           a.remove(i)

    a=''.join(a)
    print(a)

    return "".join(a)


s="abcd"
t="aacbde"
findTheDifference(s,t)
