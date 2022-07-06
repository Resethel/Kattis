#!/usr/bin/env python3
"""
Using python3.

url: https://open.kattis.com/problems/shopaholic

Explanation:
    Every 3rd items is discounted so bring the items 3 by 3 and always
    giving the by descending order of prices guarantees the maximum discount.
    Therefore, we first order the prices by descending order and then we sum up
    every third items
"""
n = int(input())
# Get the prices in a sorted by decreasing number
prices = list(sorted((int(x) for x in input().split()), reverse=True))
# Print the sum of every third items
print(sum(prices[i] for i in range(2, n, 3)))
