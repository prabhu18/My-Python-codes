class node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        self.leaf = False


class MagicDictionary:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return node()

    def return_index(self, ch):
        return ord(ch) - ord('a')

    def insert_in_trie(self, val):
        crawl = self.root
        for i in range(0, len(val)):
            index = self.return_index(val[i])

            if crawl.children[index] is None:
                crawl.children[index] = self.getNode()
            crawl = crawl.children[index]
            crawl.count = crawl.count + 1

        crawl.leaf = True

    def search_in_trie_modified_util(self, crawl, val):
        for i in range(0, len(val)):
            index = self.return_index(val[i])
            if crawl.children[index] is None:
                return False
            crawl = crawl.children[index]
        return crawl is not None and crawl.leaf

    def search(self, s):
        crawl = self.root
        for i in range(0, len(s)):
            index = self.return_index(s[i])
            for j in range(0, 26):
                if j != index and crawl.children[j] is not None:
                    if self.search_in_trie_modified_util(crawl.children[j], s[i + 1:]):
                        return True

            if crawl.children[index] is None:
                break
            else:
                crawl = crawl.children[index]
        return False

    def buildDict(self, keys):
        for i in keys:
            self.insert_in_trie(i)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)