class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        right = len(s) - 1
        left = 0
        while left < right:
            if not s[left].isalnum():
                    left += 1
            elif not s[right].isalnum():
                    right -= 1
            elif s[right] == s[left]:
                left += 1
                right -= 1
            else:
                return False
        return True