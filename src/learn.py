import nltk
from nltk import ngrams
from nltk.stem import *

stemmer = PorterStemmer()

def handle_text(countsByGram, text):
    sentences = text.split('.')
    for s in sentences:
        grams = ngrams(s.split(), 1)
        for g in grams:
            g = map_tuple(stemmer.stem, g)
            if (g not in countsByGram):
                countsByGram[g] = 0
            countsByGram[g] += 1

def map_tuple(func, tup):
    new_tuple = ()
    for itup in tup:
        new_tuple += (func(itup),)
    return new_tuple


# countsByGram = {}
# for d in data:
#     # print(d['text'])
#     _handle_text(d)
