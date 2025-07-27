import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_counts = {}
        for ch in t:
            t_counts[ch] = t_counts.get(ch, 0) + 1

        window = {}
        left = right = 0
        have, need = 0, len(t_counts)
        res, length = (0, 0), math.inf

        while right < len(s):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in t_counts and t_counts[ch] == window[ch]:
                have += 1

            while have == need:
                if right - left + 1 < length:
                    res, length = (left, right), right - left + 1

                ch = s[left]
                window[ch] = window.get(ch, 0) - 1
                if ch in t_counts and window[ch] < t_counts[ch]:
                    have -= 1

                left += 1

            right += 1

        if length == math.inf:
            return ""

        return s[res[0] : res[1] + 1]
