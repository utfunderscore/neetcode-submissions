import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)

        best = 0
        bestScore = 10000
        while l <= r:
            speed = l + ((r - l) // 2)
        
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/max(1, speed))
            
            print(speed, totalTime)

            if h >= totalTime: #
                r = speed-1
                if speed > 0:
                    best = speed
            else:
                l = speed+1
        return best


