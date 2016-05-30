def cipher(s):
    return "".join(chr(219-ord(c)) if 'a' <= c <= 'z' else c in s)

if __name__ == '__main__':
    s = "Hello, World!"

