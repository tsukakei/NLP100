s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
w = [a.strip(".,") for a in s.split()]
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}
for i, v in enumerate(w, 1):
    l = 1 if i in single else 2
    dict.update({v[:l]:i})
print dict
