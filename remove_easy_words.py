
import sys, re, string, collections, math
from termcolor import colored
from helpers import * 

wordlist = load_wordlist() 


def easy(w):
    lf = 99133.0        # PGY
    uf = 23135851162.0  # THE
    if w.upper() not in wordlist:
        return False

    # BIZJOURNALSHIRE	1602219  # 20000th word in the dictionary. 
    # Assumption here is users know all the words above that. 

    return 1602219 < wordlist[w.upper()] 


def main():
    book = collections.defaultdict(int)
    book_filename = sys.argv[1]
    for line in open(book_filename).readlines():
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        line = regex.sub('', line)
        for w in line.split():
            w = w.strip()
            if not easy(w) and w.upper() not in book: 
                book[w.upper()] = 0
                print w.upper(), 

if __name__ == '__main__':
    main()

