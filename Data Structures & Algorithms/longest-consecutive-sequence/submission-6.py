class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)
        
        output_list = []
        result_list = []
        print(nums)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            for i in range(0, len(nums)-1):
                # print(nums[i+1] - nums[i])
                if nums[i+1] - nums[i] == 1:
                    output_list.append(nums[i+1])
                elif nums[i+1] - nums[i] != 1:
                    if i+1 > len(nums)-1:
                        pass
                    else:
                        if len(output_list) > 0:
                            result_list.append(output_list)
                            # print(result_list)
                            output_list = []
            print(result_list)
            print(output_list)
            if len(result_list) == 0:
                return len(output_list) + 1 
            elif len(max(result_list, key=len)) < len(output_list):
                return len(output_list) + 1 
            else:
                return len(max(result_list, key=len)) + 1





        