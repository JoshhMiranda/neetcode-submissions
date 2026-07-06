class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     if list(s).sort == list(t).sort:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

        s = sorted(list(s))
        t = sorted(list(t))
        return s == t