#!/usr/bin/env python3
# https://open.kattis.com/problems/everywhere

T = int(input())
for _ in range(T):
    nb_of_work_trips = int(input())
    cities = [""] * nb_of_work_trips
    for work_trip in range(nb_of_work_trips):
        cities[work_trip] = input()
    print(len(set(cities)))
