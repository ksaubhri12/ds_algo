class Solution:
    def factorial(self, n):
        arr = []
        for i in range(0, n):
            element = self.get_factorial(i + 1)
            arr.append(element)

        return arr

    def get_factorial(self, n):
        if n == 0:
            return 1

        return n * self.get_factorial(n - 1)


if __name__ == '__main__':
    print(Solution().factorial(5))
