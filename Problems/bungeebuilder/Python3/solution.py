# Using python 3
# https://open.kattis.com/problems/bungeebuilder

from itertools import groupby


def find_peaks(data):
    start = 0
    sequence = []
    for key, group in groupby(data):
        sequence.append((key, start))
        start += sum(1 for _ in group)

    for (b, bi), (m, mi), (a, ai) in zip(sequence, sequence[1:], sequence[2:]):
        if b < m and a < m:
            yield mi, m
# End def find_peaks


def find_valleys(data):
    start = 0
    sequence = []
    for key, group in groupby(data):
        sequence.append((key, start))
        start += sum(1 for _ in group)

    for (b, bi), (m, mi), (a, ai) in zip(sequence, sequence[1:], sequence[2:]):
        if b > m and a > m:
            yield mi, m
# End def find_valleys


def is_peak_pair_valid(peaks, index_1, index_2):
    lowest_peak = min(peaks[index_1][1], peaks[index_2][1])
    if peaks[index_1] == peaks[index_2]:
        return False
    if abs(index_1 - index_2) > 1:
        for k in range(index_1+1, index_2):  # abandon if there is a peak to high in between the two main peaks
            if peaks[k][1] >= lowest_peak:
                return False
    return True


if __name__ == "__main__":
    N = int(input())
    height = [int(x) for x in input().split(" ")]

    # Eliminate the case were the mountains are sorted by increasing or
    # decreasing height
    if all(height[i] <= height[i + 1] for i in range(len(height)-1)) or \
       all(height[i] >= height[i + 1] for i in range(len(height)-1)):
        highest_jump = 0
    else:
        # Find all peaks and valleys
        peaks = []
        if height[0] > height[1]:  # adds the eventual first extremity
            peaks.append((0, height[0]))
        peaks += (list(find_peaks(height)))
        if height[-1] > height[-2]:  # adds the eventual last extremity
            peaks.append((len(height)-1, height[-1]))

        valleys = list(find_valleys(height))

        highest_jump = 0
        for i in range(len(peaks)-1):
            for j in range(i+1, len(peaks)):
                lowest_peak = min(peaks[i][1], peaks[j][1])
                if not is_peak_pair_valid(peaks, i, j):
                    continue
                else:
                    valley_list = (valley for valley in valleys \
                                   if valley[0] > peaks[i][0] and valley[0] < peaks[j][0])

                    for valley in valley_list:
                        highest_jump = max(highest_jump, abs(lowest_peak - valley[1]))

    print(highest_jump)
