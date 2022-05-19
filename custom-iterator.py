class Counter:
    def __init__(self, start, end, step=1):
        self.curent = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.curent < self.end:
            num = self.curent
            self.curent += self.step
            return num
        raise StopIteration


my_Counter = Counter(0, 20, 2)

for num in my_Counter:
    print(num)