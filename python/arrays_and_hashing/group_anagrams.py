from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)

        for s in strs:
            out["".join(sorted(s))].append(s)

        return list(out.values())
