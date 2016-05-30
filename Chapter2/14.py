import sys

with open("hightemp.txt", "r") as f:
    for i in range(int(sys.argv[1])):
        print f.readline(),
