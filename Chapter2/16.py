import sys
import math

n = int(sys.argv[1])
with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    l = math.ceil((len(lines) + 1) / n)
    for i in xrange(n):
        with open('16-' + str(i + 1) + '.txt', 'w') as w:
            w.write(''.join(lines[int(l*i): int(l*i + l-1)]))
            w.close()
