from typing import List
import copy
from pprint import pprint

GRID_SIZE = 8


def place_queens(row: int, columns: List[int], results: List[List[int]]):
    if row == GRID_SIZE:
        results.append(copy.deepcopy(columns))
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col):
                #  クイーンを配置
                columns[row] = col
                place_queens(row+1, columns, results)


def check_valid(columns: List[int], row1: int, column1: int):
    for row2 in range(row1):
        column2 = columns[row2]
        #  row2, column2に置かれたクイーンがrow1, column1に置くことを阻害するか判定

        # 同じ列にクイーンがあるか判定
        if column1 == column2:
            return False

        # 同じ斜め線上に他のクイーンがあるか判定
        # 2点間の列の差と行の差が等しければ同じ斜め線上にある
        # row1 > row2なので絶対値は不要
        column_distance = abs(column2 - column1)
        row_distance = row1 - row2
        if column_distance == row_distance:
            return False

    return True


if __name__ == "__main__":
    results = []
    columns = [0, 0, 0, 0, 0, 0, 0, 0]
    place_queens(0, columns, results)
    pprint(results)
