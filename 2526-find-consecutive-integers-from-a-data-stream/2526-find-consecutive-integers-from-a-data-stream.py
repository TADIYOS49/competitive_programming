class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.res = deque()

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.res.append(num)
        else:
            self.res = deque()
        if len(self.res) == self.k:
            self.res.popleft()
            return True
        else:
            return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)