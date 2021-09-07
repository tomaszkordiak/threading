import os
from os.path import isdir, join
from time import perf_counter

matches = []
number_location = 0


def file_search(root, filename):
    print("Searching in:", root)
    global number_location
    number_location += 1
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            matches.append(full_path)
        if isdir(full_path):
            file_search(full_path, filename)


def main():
    t1_start = perf_counter()
    file_search("/Users/tomaszkordiak/Documents", "delegacje_czerwiec_2019.xls")
    for m in matches:
        print("Matched:", m)
    t1_stop = perf_counter()

    print("Elapsed time:", t1_stop, t1_start)

    print("Elapsed time during the whole program in seconds:",
          t1_stop - t1_start)


main()
print("Szukano w liczbie miejsc:", number_location)
