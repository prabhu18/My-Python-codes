from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.count = 0

    def get_count(self, x, d):

        if len(x) == 0:
            self.count = self.count + 1
            return

        for i in range(1, len(x) + 1):

            temp = x[0:i]
            key = ''.join(temp)
            try:
                if d[key]:
                    self.get_count(x[i:], d)
            except:
                pass

    def numDecodings(self, s):

        if s is None and len(s) == 0:
            return 0
        l = len(s)

        prev_2 = 1

        if s[0] == '0':
            prev_1 = 0
        else:
            prev_1 = 1

        for i in range(2, l + 1):

            curr = 0
            first_val = int(s[i - 1:i])
            second_val = int(s[i - 2:i])

            if 1 <= first_val <= 9:
                curr += prev_1
            if 10 <= second_val <= 26:
                curr += prev_2

            prev_2 = prev_1
            prev_1 = curr
        return prev_1

