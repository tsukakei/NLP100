import sys
with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    for i in reversed(xrange(int(sys.argv[1]))):
        print lines[len(lines) - 1 - i],
