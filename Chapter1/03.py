s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = []
for w in s.split():
    list.append(len(w.strip(".,")))
print list
