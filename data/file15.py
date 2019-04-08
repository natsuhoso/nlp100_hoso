import sys
file = sys.argv[1]
n = int(sys.argv[2])

with open(file) as r:
    text = [(i[:-1] if i[-1] is '\n' else i) for i in  r.readlines()]

print("\n".join(text[-n:]))
