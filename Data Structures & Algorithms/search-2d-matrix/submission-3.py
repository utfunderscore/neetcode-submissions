class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        l = 0
        r = (height*width)-1

        while l <= r:
            mid = l + (r - l) // 2
            y = mid // width
            x = mid % width
            if target > matrix[y][x]:
                l = mid+1
            elif target < matrix[y][x]:
                r = mid-1
            else:
                return True
        return False