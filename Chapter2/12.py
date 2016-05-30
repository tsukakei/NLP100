with open("hightemp.txt", "r") as f, open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
    for line in f:
        col1.write(line.split()[0] + "\n")
        col2.write(line.split()[1] + "\n")
    col1.close()
    col2.close()
