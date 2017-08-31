class Solution(object):
    def lengthOfLongestSubstring(self, s):

        visited = [-1] * 256
        curr_count = 1
        max_count = 1

        if s == '':
            return 0
        visited[ord(s[0])] = 0

        for i in range(1, len(s)):

            old_value = visited[ord(s[i])]
            if old_value == -1 or i > curr_count + old_value:
                curr_count = curr_count + 1

            else:

                if curr_count > max_count:
                    max_count = curr_count
                curr_count = i - old_value

            visited[ord(s[i])] = i

        if curr_count > max_count:
            max_count = curr_count

        return max_count
