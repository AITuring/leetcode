
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    length=len(s)
    mid=int(length/2)
    start=list(s[0:mid])
    end=s[mid:]
    end=list(end[::-1])
    word = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    j=0
    for i in range(min(len(start)-1,len(end)-1)):
        if (start[i] in word) and (end[j] in word):
            temp = end[j]

            end[j] = start[i]

            start[i] = temp
        j+=1

    start=''.join(start)
    end=''.join(end)[::-1]
    str=start+end
    print(str)
    return str



s='leetcode'
t='hello'
reverseVowels(t)



