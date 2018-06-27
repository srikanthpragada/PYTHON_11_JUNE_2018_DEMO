
class Numbers:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num == 10:
            raise StopIteration

        self.num += 1
        return self.num


nums = Numbers()
for i in nums:
    print(i)

