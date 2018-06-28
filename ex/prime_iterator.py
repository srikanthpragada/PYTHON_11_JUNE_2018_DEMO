def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    else:
        return True


class PrimeNumbers:
    def __init__(self, start, end):
        self.numbers = []
        for i in range(start, end + 1):
            if is_prime(i):
                self.numbers.append(i)

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos == len(self.numbers):
            raise StopIteration
        else:
            v = self.numbers[self.pos]
            self.pos += 1
            return v

    def print_numbers(self):
        for n in self.numbers:
            print(n)


p = PrimeNumbers(100, 200)

for n in p:
    print(n, end=' ')
