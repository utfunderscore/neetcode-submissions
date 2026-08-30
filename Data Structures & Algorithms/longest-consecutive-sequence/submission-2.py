class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        best = 0

        for num in numSet:
            if (num - 1) not in numSet:
                pointer = 1
                while (num + pointer) in numSet:
                    pointer+=1
                best = max(best, pointer)

        return best



        
        