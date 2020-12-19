# Using Python 3
# https://open.kattis.com/problems/sequences
# The problem can be divided in in the sum of 3 sub problems, namely:
# 1. The number of inversions known characters times 2**nb_of_qm
# 2. The sum of inversions among the combinations of '?' characters
# 3. The sum of inversions created by each '?' characters

import itertools

# Constants and variables definition

MOD = 1000000007


# Functions definition

# Fast inversion count found at https://stackoverflow.com/questions/337664/counting-inversions-in-an-array
def count_inversion(lst):
    """Calculate the number of inversion in an array."""
    return merge_count_inversion(lst)[1]


def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int(len(lst) / 2)
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)


def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count


def fast_power(base, exp):
    """Fast power calculation using repeated squaring."""
    if exp < 0:
        return 1 / fast_power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans
# End def fast_power


# Main program

sequence = [char for char in input()]
nb_of_qm = sequence.count('?')
nb_of_01 = len(sequence) - nb_of_qm
sequence_without_qm = [int(char) for char in sequence if char in {'0', '1'}]
formatted_sequence = [char.replace('?', '{}') for char in sequence]
formatted_sequence_str = "".join(formatted_sequence)

# 1. The number of inversions among known characters times 2**nb_of_qm
pb_1_sol = count_inversion(sequence_without_qm) * fast_power(2, nb_of_qm)

# 2. The sum of inversions among the combinations of '?' characters
pb_2_sol = 0
for i in range(1, nb_of_qm):
    pb_2_sol += int((nb_of_qm-i+1)*(nb_of_qm-i)*i/2)

# 3.
pb_3_sol = 0
inv = 0
for index in range(nb_of_qm):
    replace_str = ['']*nb_of_qm
    for i in (0, 1):
        replace_str[index] = str(i)
        inv += count_inversion(formatted_sequence_str.format(*replace_str))

pb_3_sol = fast_power(2, inv)
print("str: {} inv: {}".format(formatted_sequence_str.format(*replace_str), count_inversion(formatted_sequence_str.format(*replace_str))))

print("1: " + str(pb_1_sol))
print("2: " + str(pb_2_sol))
print("3: " + str(pb_3_sol))
print("1+2+3: " + str(pb_1_sol + pb_2_sol + pb_3_sol))
