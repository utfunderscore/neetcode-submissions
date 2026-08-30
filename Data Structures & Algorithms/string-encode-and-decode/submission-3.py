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
            sizestring = ""
            foundSize = False
            while not foundSize:
                curr = s[cursor]
                cursor += 1
                if curr == '#':
                    foundSize = True
                    break
                sizestring += curr
            
            size = int(sizestring)
            word = s[cursor:cursor+size]
            cursor+=size
            words.append(word)
            

        return words



