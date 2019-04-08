import sys
file = sys.argv[1]
n = int(sys.argv[2])

with open(file) as r:
    for line in r:
        if n == 0:
            break
        print(line[:-1] if line[-1] is '\n' else line)
        n = n - 1
