class Solution(object):
    def reverseWords(self, s):
        s = list(s.rstrip().lstrip())
        s = s[::-1]
        prev = 0
        i = 0
        for i in range(0, len(s)):
            if s[i] == ' ':
                if prev != i:
                    s[prev:i] = s[prev:i][::-1]
                    prev = i + 1
                else:
                    s[i] = ''
                    prev = i + 1
            else:
                i = i + 1

        s[prev:i] = s[prev:i][::-1]
        return ''.join(s)
