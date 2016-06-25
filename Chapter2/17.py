# coding: UTF-8
with open("hightemp.txt", "r") as f:
    print('\n'.join(set(l.split()[0] for l in f.readlines())))
