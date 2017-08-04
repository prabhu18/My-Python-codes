__author__ = 'pjha'

import sys
inp = []
try:
    while True:
        inp.append(raw_input())
except:
    pass

test = inp[1:]
N = int(inp[0])
if N > 10**5:
	sys.exit(1)

#test = ["et", "eq", "bd", "be", "bdp"]

class Node:
	def __init__(self, func):
		self.increment = func
		self.children = {}
	def add(self, ch):
		try:
			n = self.children[ch]
		except:
			n = Node(self.increment)
			n.letter = ch
			self.increment()
			self.children[ch] = n
		return n

class store:
	def __init__(self):
		self.cost = 0;
		self.root = Node(self.inc)
		self.root.leter = '\0'
	def add(self, text):
		cur = self.root
		for x in text:
			try:
				cur = cur.children[x]
			except:
				cur = cur.add(x)
	def GetCost(self):
		return self.cost + 1

	def inc(self):
		self.cost = self.cost + 1
st = store()
for s in test:
	if len(s) > 30:
		sys.exit(2)
	st.add(s)

print st.GetCost()


