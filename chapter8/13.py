# 幅wi 高さhi 奥行きdi の n個の箱の山がある
# それぞれの箱は幅、高さ、奥行きのすべてが大きい箱の上に積むことしかできない
# この時高さが最大になるような積み方を計算するメソッド
import random
from typing import List
import copy

minimum = 1
maximum = 100


class Box:
    wi: int
    hi: int
    di: int

    def __init__(self):
        self.wi = random.randint(minimum, maximum)
        self.hi = random.randint(minimum, maximum)
        self.di = random.randint(minimum, maximum)

    def __str__(self):
        return f"width: {self.wi}, height: {self.hi}, depth: {self.di}"


class Calculate:
    result: List

    def __init__(self):
        self.result = []

    def calculate(self, box_list: List[Box]) -> int:
        box_list.sort(key=lambda x: x.hi)
        max_height = 0
        for i in range(len(box_list)):
            height = self._calculate(box_list, i)
            max_height = max(max_height, height)
        return max_height

    def _calculate(self, box_list: List[Box], bottom_index: int):
        bottom = box_list[bottom_index]
        max_height = 0
        for i in range(bottom_index+1, len(box_list)):
            box = box_list[i]
            if self.check(bottom, box):
                print(f"if enter bottom: {bottom}, box: {box}")
                height = self._calculate(box_list, i)
                max_height = max(height, max_height)
        max_height += bottom.hi
        return max_height

    def check(self, bottom: Box, box: Box) -> bool:
        print(f"bottom: {bottom}, box: {box}")
        return bottom.di >= box.di and bottom.wi >= box.wi and bottom.hi >= box.hi


if __name__ == "__main__":
    n = 3
    box_list = [Box() for _ in range(n)]
    for box in box_list:
        print(box)
    c = Calculate()
    height = c.calculate(box_list)
    print(height)
