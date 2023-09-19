class Solution:
    a = ord("a")
    z = ord("z")

    A = ord("A")
    Z = ord("Z")

    _0 = ord("0")
    _9 = ord("9")

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isAlphaNum(s[left]):
                left += 1
                continue

            if not self.isAlphaNum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isAlphaNum(self, c: str) -> bool:
        return (
            self.A <= ord(c) <= self.Z
            or self.a <= ord(c) <= self.z
            or self._0 <= ord(c) <= self._9
        )
