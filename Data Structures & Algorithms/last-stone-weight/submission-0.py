class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y: continue
            elif y < x:
                heapq.heappush_max(stones, x - y)

        if not stones: return 0
        return stones[0]