from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        # print(groups)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
            

        return list(groups.values())




