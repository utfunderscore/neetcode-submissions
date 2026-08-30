class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        best = 0

        for num in nums:
            curr = num + 1
            grouping = [num]
            while curr in seen:
                grouping.append(curr)
                curr += 1
            if curr - num > best:
                best = curr - num
        return best



        
        