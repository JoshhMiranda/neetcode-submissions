class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = [i if nums[i] == target else -1 for i in range(len(nums))]
        return max(result)