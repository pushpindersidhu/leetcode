class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s:
            map[c] = map.get(c, 0) + 1

        for c in t:
            if not c in map:
                return False

            if map[c] == 1:
                del map[c]
            else:
                map[c] -= 1

        return len(map.keys()) == 0
