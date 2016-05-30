with open("col1.txt", "r") as col1, open("col2.txt", "r") as col2, open("13.txt", "w") as f:
    for c1, c2 in zip(col1, col2):
        f.write(c1.strip() + "\t" +  c2.strip() + "\n")

