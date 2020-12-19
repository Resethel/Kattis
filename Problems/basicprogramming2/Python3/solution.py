#!/usr/bin/env python3
# https://open.kattis.com/problems/basicprogramming2

from collections import Counter


def action_1(N, A):
    """Print "Yes" if there are two integers x and y in A x/=y and x+y = 7777, print "No" otherwise."""
    S = set(A)
    for i in range(1, 7777):
        if i in S and 7777-i in S:
            return 'Yes'
    return 'No'
# End def action_1


def action_2(N, A):
    """Print "Unique" if all integers in A are different, print "Contains duplicate" otherwise."""
    return "Unique" if len(set(A)) == N else "Contains duplicate"
# End def action_2


def action_3(N, A):
    """Print the integer that appears more than N/2 times in a or print -1 cannot be found."""
    most_common, count = Counter(A).most_common(1)[0]
    return str(most_common) if count > N/2 else str(-1)
# End def action_3


def action_4(N, A):
    """Find and print the median(s) integer of A."""
    A_sorted = sorted(A)
    if N % 2 == 1:
        return str(A_sorted[N//2])
    else:
        return "{} {}".format(*A_sorted[N//2-1:N//2+1])
# End def action_4


def action_5(N, A):
    """Print integers in A that fall between [100...999] in sorted order."""
    return " ".join(str(x) for x in sorted(A) if 99 < x < 1000).strip()
# End def action_5


if __name__ == "__main__":
    N, t = map(int, input().split())
    data = map(int, input().split())

    actions = {
        1: action_1,
        2: action_2,
        3: action_3,
        4: action_4,
        5: action_5,
    }
    result = actions.get(t)(N, data)

    print(result)
