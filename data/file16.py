# file16.py
import sys
import numpy as np

file = sys.argv[1]
n = int(sys.argv[2])

with open(file) as r:
    text = [(i[:-1] if i[-1] is '\n' else i) for i in  r.readlines()]

rows = np.array(text)
num = 0
for i in np.array_split(rows,int(len(rows)/n)):
    with open(f'data/dir16_b/file{num}.txt', mode = 'w') as w:
        w.write("\n".join(i))
    num = num + 1
