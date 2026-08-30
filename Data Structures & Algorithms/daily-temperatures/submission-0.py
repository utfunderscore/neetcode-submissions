class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []

        for i, temp in enumerate(temperatures):
            for j in range(i, len(temperatures)):
                future_temp = temperatures[j]
                if future_temp > temp:
                    days.append(j-i)
                    break
            else:
                days.append(0)
        return days