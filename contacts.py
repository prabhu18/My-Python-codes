class node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        self.leaf = False


class Trie:
    def __init__(self):
        self.count = 0
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

    def print_all_word(self, crawl, s):

        if crawl is None:
            return
        if crawl.leaf is True:
            self.count = self.count + 1
        for i in range(0, 26):
            if crawl.children[i] is not None:
                self.print_all_word(crawl.children[i], s + chr(i + 97))

    def search_in_dictionary1(self, s):
        crawl = self.root

        for i in range(0, len(s)):
            index = self.return_index(s[i])
            try:
                crawl = crawl.children[index]
            except:
                return 0
        try:
            self.count = crawl.count
        except:
            return 0

    def search_in_dictionary(self, s):
        crawl = self.root

        for i in range(0, len(s)):
            index = self.return_index(s[i])
            try:
                crawl = crawl.children[index]
            except:
                return 0

        try:

            if crawl.leaf is True:
                self.count = self.count + 1

            for i in range(0, 26):

                if crawl.children[i] is not None:
                    self.print_all_word(crawl.children[i], s + chr(i + 97))

        except:

            return 0


T = Trie()

for i in range(0, input()):

    var = raw_input().split(' ')
    T.count = 0

    if var[0] == 'add':
        T.insert_in_trie(var[1])
    if var[0] == 'find':
        T.search_in_dictionary1(var[1])
        print T.count