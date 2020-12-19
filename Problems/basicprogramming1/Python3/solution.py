#!/usr/bin/env python3
# https://open.kattis.com/problems/basicprogramming1


def action_1(A):
    """Print 7, regardless of the content of A."""
    return 7
# End def action_1


def action_2(A):
    """Print "Bigger" if A[0]>A[1], print "Equal" if A[0]==A[1], print "Smaller" otherwise."""
    return "Bigger" if data[0] > data[1] else \
           "Equal" if data[0] == data[1] else \
           "Smaller"
# End def action_2


def action_3(A):
    """Print the median of three integers {A[0], A[1], A[2]}."""
    return sorted(A[0:3])[1]
# End def action_3


def action_4(A):
    """Print the sum of all integers in A."""
    return sum(A)
# End def action_4


def action_5(A):
    """Print the sum of all even integers in A."""
    return sum(x for x in A if x % 2 == 0)
# End def action_5


def action_6(A):
    """Perform th instructions below.

    > Apply modulo (%) 26 to each integer in A
    > Map integer 0/1/.../25 to character 'a'/'b'/.../'z'
    > Print the sequence of characters as a string (without the spaces)
    """
    return "".join(chr(97+(x % 26)) for x in A)

# End def action_6


def action_7(A):
    """Perform the instructions below.

    > Start from index i = 0
    > Jump to index i = A[i]
    > If the current index i is outside the valid bound of [0..N-1], print “Out” and stop
    > Else if the current index i is index N-1, print “Done” and stop
    > Otherwise, repeat step b
    > If doing this leads to an infinite loop, print “Cyclic” and stop
    """
    N = len(A)
    visited = [False] * N  # The list of visited places in A
    index = 0
    answer = None
    while True:
        if index < 0 or index > N-1:
            answer = "Out"
            break
        elif index == N-1:
            answer = "Done"
            break
        elif visited[index] is True:
            answer = "Cyclic"
            break
        else:
            visited[index] = True
            index = A[index]

    return answer

# End def action_7


if __name__ == "__main__":
    N, t = (int(x) for x in input().split(" "))
    data = [int(x) for x in input().split(" ")]

    actions = {
        1: action_1,
        2: action_2,
        3: action_3,
        4: action_4,
        5: action_5,
        6: action_6,
        7: action_7,
    }
    result = actions.get(t)(data)

    print(result)
