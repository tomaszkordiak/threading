import os
from threading import Lock, Thread
from os.path import isdir, join
from time import perf_counter

from wait_group import WaitGroup

mutex = Lock()
matches = []
number_location = 0


def file_search(root, filename, wait_group):
    print("Searching in:", root)
    global number_location
    mutex.acquire()
    number_location += 1
    mutex.release()
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=(full_path, filename, wait_group))
            t.start()
    wait_group.done()


def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t1_start = perf_counter()
    t = Thread(target=file_search, args=("/Users/tomaszkordiak/Documents", "delegacje_czerwiec_2019.xls", wait_group))
    t.start()
    wait_group.wait()
    for m in matches:
        print("Matched:", m)
    t1_stop = perf_counter()

    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",
          t1_stop - t1_start)


main()
print("Szukano w liczbie miejsc:", number_location)
