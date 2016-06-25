from random import shuffle
def typoglycemia(word): 
    if len(word) < 4:
        return word
    mid_word = list(word[1:-1])
    shuffle(mid_word)
    return word[0] + "".join(mid_word) + word[-1]

if __name__ == '__main__':
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print " ".join(typoglycemia(w.strip(".,")) for w in s.split())
