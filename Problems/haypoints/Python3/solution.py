# Using Python 3
# https://open.kattis.com/problems/haypoints

M, N = map(int, input().split(" "))
Jobs = dict()
# getting the jobs
for _ in range(M):
    job, hay_points = input().split(" ")
    Jobs[job] = int(hay_points)

for _ in range(N):
    job_desc = ""
    points = 0
    line = ""
    while line != ".":
        line = input().strip()
        points += sum([Jobs[x] for x in line.split(" ") if x in Jobs])
    print(points)
