class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            length = len(word)
            print(word, length)
            output += str(length)
            output += '#'
            output += word
        return output


    def decode(self, s: str) -> List[str]:
        cursor = 0
        length = len(s)

        if length == 0:
            return []

        words = []

        while cursor < length:
            j = cursor
            while s[j] != '#':
                j += 1
            size = int(s[cursor:j])
            cursor = j+1
            word = s[cursor:cursor+size]
            cursor = cursor+size
            words.append(word)
            

        return words



