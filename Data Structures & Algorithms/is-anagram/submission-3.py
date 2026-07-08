class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     if set(s) ==  set(t):
        #         return True
        #     else:
        #         return False
        
        # else:
        #     return False

        # print(sorted(list(s)))
        dict1 = dict()
        dict2 = dict()
        for word in sorted(list(s)):
            if word in dict1.keys():
                dict1[word] = dict1[word] + 1
            else:
                dict1[word] = 1

        for word in sorted(list(t)):
            if word in dict2.keys():
                dict2[word] = dict2[word] + 1
            else:
                dict2[word] = 1

        if dict1 == dict2:
            return True
        else:
            return False
