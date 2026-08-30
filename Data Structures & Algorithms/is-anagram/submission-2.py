class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data = {}

        for l in s:
            data[l] = data.get(l, 0) + 1
        
        print(data)

        for l in t:
            new = data.get(l, 0) - 1

            if data.get(l, 0) - 1 < 0:
                return False

            data[l] = new

        for d, e in data.items():
            if e > 0:
                return False

        return True