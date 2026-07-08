import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        s = s.lower()
        if list(s) == list(s)[::-1]:
            return True
        else:
            return False

        
        