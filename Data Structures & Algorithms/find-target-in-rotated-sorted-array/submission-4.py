class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        n = len(nums)

        l = 0
        r = n-1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        mini = l

        if mini == 0:
            l = 0
            r = n-1
        elif target >= nums[0] and target <= nums[mini-1]:
            l = 0
            r = mini-1
        elif target >= nums[mini] and target <= nums[n-1]:
            l = mini
            r = n-1

        while l <= r:
            mid = (l+r) // 2
            midv = nums[mid]

            if midv == target:
                return mid
            elif target > midv:
                l = mid+1
            else:
                r = mid-1

        
        return -1

        