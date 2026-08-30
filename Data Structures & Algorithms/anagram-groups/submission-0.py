class Solution:
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for word in strs:
            frequencies = [0] * 26
            for c in word:
                frequencies[ord(c) - ord('a')] += 1
            output[tuple(frequencies)].append(word)
        return list(output.values())

        