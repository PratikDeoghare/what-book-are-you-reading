


import sys, re, string, collections, math
from nltk.tokenize import RegexpTokenizer

color_dict = {
        0 : 'red', 
        1 : 'yellow', 
        2 : 'green', 
        3 : 'magenta', 
        4 : 'blue', 
        5 : 'cyan',
        6 : 'grey',
        7 : 'white', 
        8 : 'white'
}

def load_wordlist(wordlist_filename = 'wordlist.txt'):
    wordlist = collections.defaultdict(int)
    
    for line in open(wordlist_filename).readlines():
        word, freq = line.split() 
        word = word.strip()
        freq = int(freq.strip())
        wordlist[word] = freq 
    return wordlist 

def read_book(filename):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(open(filename).read())
 

def test():
    pass 

if __name__ == '__main__':
    test()
