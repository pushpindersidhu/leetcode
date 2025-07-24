class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        map = {}
        longest = start = 0
        for i in range(len(s)):
            if s[i] in map and map[s[i]] >= start:
                start = map[s[i]] + 1
            longest = max(longest, i - start)
            map[s[i]] = i

        return longest + 1
