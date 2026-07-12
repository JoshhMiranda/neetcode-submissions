class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # print(stones)
        # stones = sorted(stones)
        # print(stones)
        if len(stones) == 1:
            return 1
               
        while len(stones) > 1:
            stones = sorted(stones)
            # print(stones)
            # print(stones[-1], stones[-2], stones[-1] - stones[-2])
            t = stones[-1] - stones[-2]
            stones = stones[:-2]
            stones.append(t)
            print(stones)
            # print(len(stones))
            # print("xx")

            if len(stones) == 1:
                return stones[0]
                break
