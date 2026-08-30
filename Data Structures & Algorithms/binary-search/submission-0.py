class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False

        upper = len(nums)-1
        lower = 0

        while lower <= upper:
            mid = lower + ((upper-lower) // 2)
            value = nums[mid]

            if value > target:
                upper = mid -1
            elif value < target:
                lower = mid + 1
            else:
                return mid
        return -1


        