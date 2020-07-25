from typing import List


class Case:
    result = dict()

    def count(self, n: int) -> int:
        self.result = dict()
        self._count(n, 0, 0, 0, 0)
        return sum(self.result.values())

    def _count(self, n: int, num25: int, num10: int, num5: int, num1: int):
        key = f"25: {num25}, 10: {num10}, 5: {num5}, 1: {num1}"
        if key in self.result:
            return

        total = 25 * num25 + 10 * num10 + 5 * num5 + 1 * num1
        if n == total:
            self.result[key] = 1
            return
        elif n < total:
            return

        self._count(n, num25+1, num10, num5, num1)
        self._count(n, num25, num10+1, num5, num1)
        self._count(n, num25, num10, num5+1, num1)
        self._count(n, num25, num10, num5, num1+1)


if __name__ == "__main__":
    case = Case()
    assert case.count(10) == 4
    assert case.count(8) == 2
    assert case.count(15) == 6
    assert case.count(25) == 13
    assert case.count(30) == 18