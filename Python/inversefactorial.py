# Using Python 3
# https://open.kattis.com/problems/inversefactorial

# The naive approach for calculating inv(n!) may take to much time for really
# big numbers.
# However we know that the number of digit in a factorial is unique after 9!
# (because for each factorial, we always multiply the previous factorial by a number > 10)
# and we know that the number of digits is given by log10(x)+1 if x is a power of 10
# or ceil(log10(x)) otherwise. Or the only factorial numbers that are a power of 10 are 0! and 1!
# since 2! isn't and the rest have 3 as a factor.
#
# So the solution consist in checking that the amount of digit of the input number is
# equal to log10(n!). To do so, we use the following identity:
# log10(n!) = log10(1 * 2 * ... * n) = log10(1) + log10(2) + ... + log(n)
#
# It is also important to note that there are cases in the early number that are
# not unique, so for those we just compare them with known solutions.


import math

known_solutions = {
    "1":      1,
    "2":      2,
    "6":      3,
    "24":     4,
    "120":    5,
    "720":    6,
    "5040":   7,
    "40320":  8,
    "936880": 9,
}
N = input().strip()

if N in known_solutions:
    print(known_solutions[N])
else:
    digits = len(N)
    log_sum = sum([math.log10(x) for x in range(1, 10)])
    solution = 9
    while math.ceil(log_sum) < digits:
        solution += 1
        log_sum += math.log10(solution)

    print(solution)
