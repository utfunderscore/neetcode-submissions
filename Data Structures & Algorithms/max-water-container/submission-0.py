class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1

        best = 0

        while l <= r:
            lv = heights[l]
            rv = heights[r]
            area = (r-l)*min(lv, rv)
            print(area)

            if area > best:
                best = area

            if lv < rv:
                l+=1
            else:
                r-=1
        return best