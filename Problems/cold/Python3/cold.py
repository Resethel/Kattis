#!/usr/bin/env python3
"""
Using Python 3.

url: https://open.kattis.com/problems/cold
"""

input()  # Discard the first input
print(sum(int(x) < 0 for x in input().split()))
