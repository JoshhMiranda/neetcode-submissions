class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        overall_list = []
        for i in matrix:
            for j in i:
                overall_list.append(j)
        
        return target in overall_list