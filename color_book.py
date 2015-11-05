


import sys, re, string, collections, math
from termcolor import colored
from helpers import * 

book_filename = sys.argv[1]
wordlist = load_wordlist() 

def color_line(line):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    line = regex.sub('', line)

    lf = 99133.0        # PGY
    uf = 23135851162.0  # THE

    color_number = lambda w : int(math.ceil((wordlist[w] - lf) / (uf - lf) * 8))
    get_color = lambda w : color_dict[color_number(w)]

    return [(word, get_color(word.upper())) for word in line.split()] 

def main():
    for line in open(book_filename).readlines():
        for w in color_line(line):
            print colored(*w), 
        print 

if __name__ == '__main__':
    main()

