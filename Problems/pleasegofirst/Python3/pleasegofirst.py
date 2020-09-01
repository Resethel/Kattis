# Using Python3
# https://open.kattis.com/problems/pleasegofirst


def get_total_wait(_queue):
    # Return the combined waiting time of everybody

    n = len(_queue)
    last = 256*[-1]     # List of group's last person position in the queue (List of 256 ASCII)
    for i in range(n):  # Fill the groups' last person in the queue position
        last[ord(_queue[i])] = i

    total_wait = 0
    for i in range(n):
        # for each person, we add its total waiting time
        total_wait += 5 * (last[ord(_queue[i])] - i)

    # Then we return the combined waiting time of everybody in the queue
    return total_wait
# End def compute_time


# =====( Main loop )======================================================== #

N = int(input())  # Number of Cases
for _ in range(N):
    n = int(input())  # Number of person in the queue
    queue_n = input()

    # print saved time
    print(get_total_wait(queue_n) - get_total_wait(sorted(queue_n)))
