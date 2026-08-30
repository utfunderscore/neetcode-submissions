import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        best = 0
        while l <= r:
            speed = (r + l) // 2
        
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/speed)

            if h >= totalTime: #
                r = speed-1
                best = speed
            else:
                l = speed+1
        return best


