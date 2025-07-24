class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = maxf = left = right = 0
        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxf = max(maxf, counts[s[right]])
            window = right - left + 1
            if window - maxf > k:
                counts[s[left]] -= 1
                left += 1
            else:
                res = max(res, window)
            right += 1

        return res
