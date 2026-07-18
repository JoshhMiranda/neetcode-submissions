import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            multiplier = 1
            result.append(
                math.prod(
                   [nums[j] for j in range(len(nums)) if j !=i]
                    )
                )
            
        return result