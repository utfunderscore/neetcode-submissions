class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set([])
        best = 0

        left = 0
        right = 0

        while right < len(s):
            char = s[right]

            print(left, right)
            if char in seen:
                while char in seen:
                    seen.remove(s[left])
                    left+=1
            best = max(best, right-left+1)
            seen.add(char)
            right+=1

        return best



        