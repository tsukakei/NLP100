with open("hightemp.txt", 'r') as f:
    lines = f.readlines()
    sorted(lines, key=lambda x:x.split()[2], reverse=True)
    print "".join(lines)
