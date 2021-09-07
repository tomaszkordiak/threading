import os
from threading import Lock, Thread
from os.path import isdir, join
from time import perf_counter

mutex = Lock()
matches = []
number_location = 0


def file_search(root, filename):
    print("Searching in:", root)
    child_threads = []
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
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)
        for t in child_threads:
            t.join()


def main():
    t1_start = perf_counter()
    t = Thread(target=file_search, args=("/Users/tomaszkordiak/Documents", "delegacje_czerwiec_2019.xls"))
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)
    t1_stop = perf_counter()

    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",
          t1_stop - t1_start)


main()
print("Szukano w liczbie miejsc:", number_location)
