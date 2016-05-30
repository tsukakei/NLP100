import sys
with open("hightemp.txt", "r") as f:
    lines = f.readlines()[::-1]
    for i in range(int(sys.argv[1])):
        print lines[i],
