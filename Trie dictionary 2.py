class trienode:
    def __init__(self):
        self.count=0
        self.children=[None]*26
        self.leaf=False
        self.count=0

class Trie:
    def __init__(self):
        self.root=self.get_node()

    def get_node(self):
        return trienode()

    def char_index(self,ch):
        return ord(ch)-97

    def add_element_in_trie(self,element):
        crawl=self.root
        for i in range(0,len(element)):
            index=self.char_index(element[i])
            if crawl.children[index] is None:
                crawl.children[index]=self.get_node()
            crawl=crawl.children[index]
            crawl.count=crawl.count+1
        crawl.leaf=True


    def search_in_trie(self,element):
        crawl=self.root
        for i in range(0,len(element)):
            index=self.char_index(element[i])
            if crawl.children[index] is None:
                return False
            crawl=crawl.children[index]
        return crawl and crawl.leaf is True

    def print_array_common_prefix(self,a):
        crawl=self.root
        flag=1
        s=''
        while(flag):
            for i in range(0,26):
                if crawl.children[i] is not None:
                    if crawl.children[i].count == len(a):
                        s=s+chr(97+i)
                        break
                    else:
                        flag=0
                        break
            crawl=crawl.children[i]
        return s


T=Trie()

a=['prabhat','pradeep','praveen','pha']

for i in a:
    T.add_element_in_trie(i)

z=T.print_array_common_prefix(a)
if len(z)==0:
    print 'No prefix exist'
else:
    print z







'''
if T.search_in_trie('pravien') :
    print 'YES'
else:
    print 'NO'
'''
