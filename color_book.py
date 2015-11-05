


import sys, re, string, collections, math
from termcolor import colored
from helpers import * 

book_filename = sys.argv[1]
wordlist = load_wordlist() 

def color_word(word):

    lf = 99133.0        # PGY
    uf = 23135851162.0  # THE

    color_number = lambda w : int(math.ceil((wordlist[w] - lf) / (uf - lf) * 8))
    get_color = lambda w : color_dict[color_number(w)]

    return (word, get_color(word.upper()))

def main():
    for w in read_book(book_filename): 
        w = color_word(w) 
        print colored(*w), 

if __name__ == '__main__':
    main()

