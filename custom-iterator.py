class Counter:
    def __init__(self, start, end):
        self.curent = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.curent < self.end:
            num = self.curent
            self.curent += 1
            return num
        raise StopIteration


my_Counter = Counter(0, 20)

for num in my_Counter:
    print(num)