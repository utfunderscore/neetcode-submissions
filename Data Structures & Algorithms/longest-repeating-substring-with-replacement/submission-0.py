class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {}
        l = 0

        replacements = 0
        best = 0

        for r in range(len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1
            replacements = max(replacements, counts[char])
            
            if (r - l + 1) - replacements > k:
                counts[s[l]]-=1
                l+=1

            best = max(best, r - l + 1)
        return best
            

        