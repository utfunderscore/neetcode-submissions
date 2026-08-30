class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        occurance = [[] for i in range(len(nums) + 1)]

        print(occurance)

        for n, c in frequencies.items():
            print(c)
            occurance[c].append(n)

        print("occurance:", occurance)

        output = []
        for i in range(len(occurance))[::-1]:
            output.extend(occurance[i])
            if len(output) == k:
                return output
        return []

