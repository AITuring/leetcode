import string
def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    mapping = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    return len(set("".join(map(lambda x: mapping[ord(x) - ord('a')], i)) for i in words))

words = ["gin", "zen", "gig", "msg"]
uniqueMorseRepresentations(words)




