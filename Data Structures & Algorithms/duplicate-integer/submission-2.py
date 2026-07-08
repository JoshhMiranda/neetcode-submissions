class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False 
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #     # print(nums[i])
        #         if nums[i] == nums[j]:
        #             flag = True

        if len(nums) != len(list(set(nums))):
            flag = True

        return flag