import re
noun= 'i heard the arch'
print re.search('[^caeioudgkprt]h$', noun)