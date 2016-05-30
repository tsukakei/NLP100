s = "I am an NLPer"
charGram = [s[i:i+2] for i in range(len(s) - 1)]
w = s.split()
wordGram = ["-".join(w[i:i+2]) for i in range(len(w))]
print charGram
print wordGram
