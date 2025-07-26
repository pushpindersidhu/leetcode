class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        for c1 in s1:
            s1_counts[c1] = s1_counts.get(c1, 0) + 1

        idx = 0
        window = len(s1)
        while idx + window <= len(s2):
            s2_counts = {}
            for c2 in s2[idx : idx + window]:
                s2_counts[c2] = s2_counts.get(c2, 0) + 1

            idx += 1

            if s1_counts == s2_counts:
                return True

        return False
