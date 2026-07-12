class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        result = []
        for n in nums:
            if n not in count_dict.keys():
                count_dict[n] = 1
            else:
                count_dict[n] = count_dict[n] + 1
        
        result_list = sorted(count_dict.items(), key = lambda item: item[1], reverse=True)
        for i in range(0,k):
            result.append(result_list[i][0])
        return result
