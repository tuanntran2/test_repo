import os


def get_square(value: int) -> int:
    return value ** 2


def get_factorial(value: int) -> int:
    if value in [0, 1]:
        return 1
    return value * get_factorial(value - 1)


if __name__ == "__main__":
    num = os.environ.get("INPUT_NUM")
    print(f"result::{get_square(int(num))}")
