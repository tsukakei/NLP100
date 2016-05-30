import shuffle from random
def typoglycemia(word): 
    if len(word) < 4:
        return word
    mid_word = word[1:-1]
    shuffle(mid_word)
    return word[0] + mid_word + word[-1]

