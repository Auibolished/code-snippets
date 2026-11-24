#!/usr/bin/env python3
"""掷骰子：模拟掷 N 个 M 面骰子，输出每次点数和总和。

用法:
    python3 dice.py [个数，默认 2] [面数，默认 6]
"""
import random
import sys


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    sides = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    rolls = [random.randint(1, sides) for _ in range(n)]
    print(f"掷出: {rolls}，总和: {sum(rolls)}")


if __name__ == "__main__":
    main()
