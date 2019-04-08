# file15.py
import sys
file = sys.argv[1]
n = int(sys.argv[2])

temps = []
with open('data/hightemp.txt') as r:
    for line in r:
        temps.append((line[:-1] if line[-1] is '\n' else line).split('\t'))
hightemp =temps
print("\n".join(hightemp[-n:]))
