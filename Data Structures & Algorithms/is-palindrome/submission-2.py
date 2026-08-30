class Solution:

    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s)-1

        if a == b:
            return True

        while a <= b:
            first = s[a]
            second = s[b]
            while not first.isalnum():
                a+=1
                if a > len(s)-1:
                    break
                first = s[a]
            while not second.isalnum():
                b-=1
                second = s[b]
                if b < 0:
                    break
            if first.lower() != second.lower():
                print(first, second)
                return False
            a+=1
            b-=1

        return True
        