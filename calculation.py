import os


def get_square(value: int) -> int:
    return value ** 2


if __name__ == "__main__":
    num = os.environ.get("INPUT_NUM")
    print(f"result::{get_square(int(num))}")
