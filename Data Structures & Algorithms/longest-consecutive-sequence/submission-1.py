class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        bestset = set([])
        best = 0

        for num in nums:
            if num in bestset:
                continue
            curr = num + 1
            grouping = set([num])
            while curr in seen:
                grouping.add(curr)
                curr += 1
            curr = num - 1
            while curr in seen:
                grouping.add(curr)
                curr -= 1

            length = len(grouping)
            if length > best:
                best = length
                bestset = grouping

        return best



        
        