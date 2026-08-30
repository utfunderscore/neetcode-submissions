class Solution:

    

    def isValid(self, s: str) -> bool:

        closing = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []

        chars = list(s)

        for c in chars:
            if c in closing.keys():
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != closing.get(c):
                    print("not matching", top)
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            print("empty stack")
            return True
        return False






        