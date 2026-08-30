class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = sorted(list(s))
        t_chars = sorted(list(t))

        return s_chars == t_chars