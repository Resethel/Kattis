# Using Python 3
# https://open.kattis.com/problems/aplusb

# First of all, because there are negative numbers, make them all positive
# numbers under translation. Use an array to mark the number of occurrences of
# each number.
# Use FFT to self-convolve to get the solution that each number can be obtained
# after adding two numbers. Count (remember to subtract the contribution of the
# same number), then enumerate each number, add the answer to the two numbers to
# get the number of plans for the number, remember to subtract the case where 1
# number is 0.

import math
from collections import Counter


def fft(seq):
    """Recursively calculate the FFT of a sequence."""
    n = len(seq)  # seq is the input coefficient vector

    # recursivity final condition
    if n == 1:
        return seq

    i = 1j  # complex i
    wn = math.e ** (-2 * i * math.pi / float(n))  # wn is principle complex nth root of unity.

    A0 = list()  # even indexed coefficients
    A1 = list()  # un-even indexed coefficients
    for i in range(n):
        A0.append(seq[i]) if i % 2 == 0 else A1.append(seq[i])

    # recursive call to FFT
    Y0 = fft(A0)  # local array
    Y1 = fft(A1)  # local array

    # Storing the values
    Y = [0]*n
    w = 1
    for k in range(0, n//2):
        Y[k] = Y0[k] + w * Y1[k]
        Y[k + n // 2] = Y0[k] - w * Y1[k]
        w *= wn

    return Y
# End def fft


def ifft(seq):
    """Calculate the reverse FFT of a sequence."""
    n = len(seq)  # seq is the input coefficient vector

    # recursivity final condition
    if n == 1:
        return seq

    i = 1j  # complex i
    wn = math.e ** (2 * i * math.pi / float(n))  # wn is principle complex nth root of unity.

    Y0 = list()  # even indexed coefficients
    Y1 = list()  # un-even indexed coefficients
    for i in range(n):
        Y0.append(seq[i]) if i % 2 == 0 else Y1.append(seq[i])

    # recursive call to RFFT
    A0 = ifft(Y0)  # local array
    A1 = ifft(Y1)  # local array

    A = [0]*n
    w = 1
    for k in range(0, n//2):
        A[k] = A0[k] + w * A1[k]
        A[k + n // 2] = A0[k] - w * A1[k]
        w = w * wn

    return [x/float(n) for x in A]
# End def ifft


def fft_convolution(seq_a, seq_b):
    """Calculate the convolution of two sequences, using FFT."""
    # 1. Perform the FFT of seq_a and the reversed seq_b
    array_A = fft(seq_a)
    array_B = fft(seq_b)

    result = list()
    for i in range(len(array_A)):
        result.append(array_A[i] * array_B[i])

    result = [int(x.real+0.5) if x.real > 0 else int(x.real-0.5) for x in list(reversed(ifft(result)))]
    return result
# End def fft_convolution


OFFSET = 50001  # value added to all numbers to avoid having negative numbers

if __name__ == "__main__":

    N = int(input())
    values = [int(x) + OFFSET for x in input().split(' ')]

    # Count every unique numbers
    frequency = list(Counter(values).values())
    print("frequency: {}".format(frequency))

    # Count all zeroes
    nb_of_zeroes = values.count(0 + OFFSET)
    print("zeroes: {}".format(nb_of_zeroes))

    # Perform a convolution of the frequency array with itself to get the the
    # number of unique interactions
    results = fft_convolution(frequency, list(reversed(frequency)))
    print("convolution result: {}".format(results))

    # For each number, remove the illegal case were the number interact with
    # itself (i.e. forbid i+i=k. only allow i+j=k)
    results = [x-1 for x in results]
    print("result - interactions: {}".format(results))

    # For each number in the input, add the number of ways we can add two numbers to get it
    answer = sum(results)

    # Remove the number of ways zeroes can be added to all other numbers
    answer -= 2 * nb_of_zeroes * (N-1)

    print(answer)
