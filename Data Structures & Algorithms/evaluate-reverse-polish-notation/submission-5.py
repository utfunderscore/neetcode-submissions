class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numbers = []
        for token in tokens:
            if token == '*':
                numbers.append(numbers.pop() * numbers.pop())
            elif token == '+':
                numbers.append(numbers.pop() + numbers.pop())
            elif token == '-':
                a, b = numbers.pop(), numbers.pop()
                numbers.append(b - a)
            elif token == '/':
                a, b = numbers.pop(), numbers.pop()
                numbers.append(int(float(b) / a))
            else:
                numbers.append(int(token))
        return int(numbers[0])