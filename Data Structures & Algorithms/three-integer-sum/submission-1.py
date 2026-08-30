class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        solutions = []
        for i, num in enumerate(nums):
            if num > 0:
                break

            target = nums[i]
            if i != 0 and nums[i-1] == target:
                continue
            
            l = i+1
            r = len(nums)-1

            target = 0-target

            while l < r:
                lv = nums[l]
                rv = nums[r]
                total = lv + rv
                if total > target:
                    r-=1
                elif total < target:
                    l+=1
                else:
                    l+=1
                    r-=1
                    solutions.append([num, lv, rv])
                    while l < r and nums[r] == rv:
                        r-=1
        return solutions



