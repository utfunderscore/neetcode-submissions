class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) > 0:
                (index, value) = stack[-1]
                if value < temp:
                    stack.pop()
                    days[index] = i-index
                else:
                    break
            stack.append((i, temp))
        
        while len(stack) > 0:
            (index, value) = stack.pop()
            days[index] = 0
                
        return days


