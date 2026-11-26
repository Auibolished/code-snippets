#!/usr/bin/env python3
"""head：打印文件的前 N 行，默认 10 行，大文件也不全读进内存。

用法:
    python3 head.py <文件> [-n 行数]
"""
import argparse
import itertools


def main():
    parser = argparse.ArgumentParser(description="打印文件前 N 行")
    parser.add_argument("file", help="要查看的文件")
    parser.add_argument("-n", type=int, default=10, help="行数（默认 10）")
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as f:
        for line in itertools.islice(f, args.n):
            print(line, end="")


if __name__ == "__main__":
    main()
