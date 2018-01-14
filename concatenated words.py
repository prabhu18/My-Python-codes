def findAllConcatenatedWordsInADict(words):

    res = []
    words_dict = set(words)
    for word in words:
        words_dict.remove(word)
        if check(word, words_dict) is True:
            res.append(word)
        words_dict.add(word)
    return res

def check(word, d):
    if word in d:
        return True

    for i in range(len(word), 0, -1):
        if word[:i] in d and check(word[i:], d):
            return True
    return False

a=["cat","cats","catsdogcats","dog"]
print findAllConcatenatedWordsInADict(a)