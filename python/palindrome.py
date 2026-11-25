#!/usr/bin/env python3
"""判断字符串是不是回文（正反读都一样）。

用法:
    python3 palindrome.py <字符串>
"""
import sys


def is_palindrome(s):
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


if __name__ == "__main__":
    s = sys.argv[1] if len(sys.argv) > 1 else "level"
    print(s, "是回文" if is_palindrome(s) else "不是回文")
