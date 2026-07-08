class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = list(set(nums))
        # print(t)
        for t in temp:
            if nums.count(t) == 1:
                return t