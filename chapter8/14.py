from typing import List


def count_eval(s: str, result: bool) -> int:
    if not s:
        return 0
    if len(s) == 1:
        return 1 if str_to_bool(s) == result else 0

    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i+1:]

        left_true = count_eval(left, True)
        left_false = count_eval(left, False)
        right_true = count_eval(right, True)
        right_false = count_eval(right, False)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == "^":
            total_true = left_true * right_false + left_false * right_true
        elif c == "&":
            total_true = left_true * right_true
        elif c == "|":
            total_true = left_true * right_true + left_false * right_true + left_true * right_false

        sub_ways = total_true if result else total - total_true
        ways += sub_ways

    return ways


def str_to_bool(s: str):
    return True if s == "1" else False


if __name__ == "__main__":
    ways = count_eval("0|1", True)
    print(ways)
