x = "paraparaparadise"
y = "paragraph"
X = set([x[i:i+2] for i in range(len(x) - 1)])
Y = set([y[i:i+2] for i in range(len(y) - 1)])
Union = X|Y
Diff = X - Y
Intersection = X&Y
