"""
Input: words[] = { "may", "student", "students", "dog",
                 "studentssess", "god", "cat", "act",
                 "tab", "bat", "flow", "wolf", "lambs",
                 "amy", "yam", "balms", "looped",
                 "poodle"};
Output :
looped, poodle,
lambs, balms,
flow, wolf,
tab, bat,
may, amy, yam,
student, students, studentssess,
dog, god,
cat, act,

"""

def get_key(word):
    visited=[False]*26
    key=''
    for i in range(0,len(word)):
        visited[ord(word[i])-ord('a')]=True
    for j in range(0,len(visited)):
        if visited[j]:
            key=key+chr(ord('a')+j)

    return key


word_list=[]
Hash_words={}
for i in range(0,input()):
    word=raw_input()
    word_list.append(word)
    key=get_key(word)

    try:
        Hash_words[key].append(i)
    except:
        Hash_words[key]=[i]

for key,value in Hash_words.iteritems():

    if len(value)>=2:
        for j in value:
            print word_list[j]+',',
    print ''

