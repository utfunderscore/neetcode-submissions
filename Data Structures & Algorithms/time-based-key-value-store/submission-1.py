class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        current = self.data.get(key, [])
        current.append([timestamp, value])
        self.data[key] = current


    def get(self, key: str, timestamp: int) -> str:
            current = self.data.get(key, [])

            print(current)

            l = 0
            r = len(current)-1

            bestvalue = ""

            while l <= r:
                mid = (l + r) // 2
                value = current[mid]

                if value[0] > timestamp:
                    r = mid-1
                elif value[0] < timestamp:
                    bestvalue = value[1]
                    l = mid+1
                else:
                    return value[1]
            return bestvalue


        
