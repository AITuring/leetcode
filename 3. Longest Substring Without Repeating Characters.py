# 在一个字符串中找到最长的不重复的子串
def lengthOfLongestSubstring(s: str) -> int:
    length = len(s)
    a,b=0,1
    count=1
    max=0
    word=[]
    word.append(s[0])
    # for i in range(1,length):
    #     if s[i]==word[-1]:

    return len(word)





if __name__ == "__main__":
    a = 'pwwkew'
    b='dvdf'
    print(lengthOfLongestSubstring(a))
