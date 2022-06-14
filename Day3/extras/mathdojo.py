class MathDojo:
    def __init__(self):
        self.result = 0
        
    def add(self, num, *nums):
        self.result += num
        print(f"Adding {num}, total: {self.result}")
        for i in nums:
            self.result += i
            print(f"Adding {i}, total: {self.result}")
        return self

    def subtract(self, num, *nums):
        self.result -= num
        print(f"Subtracting {num}, total: {self.result}")
        for i in nums:
            self.result -= i
            print(f"Subtracting {i}, total: {self.result}")
        return self

test = MathDojo()
test.add(3, 2, 4, 5).subtract(5, 4, 2, 3).subtract(3, 2, 1).add(7, 2, 3).add(1, 9, 27).subtract(18, 2, 21, 2)


