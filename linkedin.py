import curses.ascii
import json
import operator
import urllib.request
import time
import ssl
from threading import Thread


def count_letters(url, frequency):
    response = urllib.request.urlopen(url, context=ssl._create_unverified_context())
    txt = str(response.read())
    for w in txt.split():
        word = w.lower()

        if any(not c.isalnum() for c in word) or (len(word) < 4):
            continue

        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1


def main():
    frequency = {}
    start = time.time()
    count_letters(f"https://www.wykop.pl/ludzie/wykopowy_brukselek/", frequency)
    end = time.time()
    frequency_sorted = dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True))
    print(json.dumps(frequency_sorted, indent=4))
    print("Done, time taken", end - start)


main()
