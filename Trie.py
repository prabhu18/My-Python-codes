class node:
    def __init__(self):
        self.children=[None]*26
        self.count=0
        self.leaf=False

class Trie:
    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return node()

    def return_index(self,ch):
        return ord(ch)-ord('a')

    def insert_in_trie(self,val):
        crawl=self.root
        for i in range(0,len(val)):
            index=self.return_index(val[i])

            if crawl.children[index] is None:
                crawl.children[index]=self.getNode()
            crawl = crawl.children[index]
            crawl.count=crawl.count+1

        crawl.leaf=True



    def search_in_trie(self,val):
        crawl=self.root

        for i in range(0,len(val)):
            index = self.return_index(val[i])

            if crawl.children[index] is None:
                return False
            crawl = crawl.children[index]
        return crawl is not None and crawl.leaf

    def unique_prefix(self,c):
        crawl=self.root
        s=''
        for i in range(0,len(c)):
            index=self.return_index(c[i])
            if crawl.count==1:
                return s
            s=s+c[i]
            crawl=crawl.children[index]

        return s

    def print_all_word(self,crawl,s):

        if crawl is None:
            return
        if crawl.leaf is True:
            print s
        for i in range(0,26):
            if crawl.children[i] is not None:
                self.print_all_word(crawl.children[i],s+chr(i+97))

    def search_in_dictionary(self,s):
        crawl=self.root

        for i in range(0,len(s)):
            index=self.return_index(s[i])
            try:
                crawl=crawl.children[index]
            except:
                print "No such word"
                return

        try:

            if crawl.leaf is True:
                print s

            for i in range(0,26):

                    if crawl.children[i] is not None:
                        self.print_all_word(crawl.children[i],s+chr(i+97))

        except:

            print "No such word"
            return





T=Trie()

keys = ["prabhat","Gayatri","sanika","sananya","sanang"]

for i in keys:
    T.insert_in_trie(i)
"""
if T.search_in_trie('yash'):
    print "Found"
else:
    print 'Not Found'

c='zebra'

if T.search_in_trie(c) is True:
    print T.unique_prefix(c)
else:
    print 'Not in directory'
"""

search_index='sa'
T.search_in_dictionary(search_index)