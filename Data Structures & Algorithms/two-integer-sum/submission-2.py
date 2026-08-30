class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for n, num in enumerate(nums):
            seen[num] = n

        for n, num in enumerate(nums):
            diff = target - num

            index = seen.get(diff, -1)

            if index != -1 and index != n:
                if n > index:
                    return [index, n]
                return [n, index]
        
        return [0, 0]



        