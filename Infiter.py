class Infiter:
    """Infinite iterator to run all odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

num = iter(Infiter())

for next in num:
    print(next)
