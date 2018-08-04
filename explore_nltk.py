import nltk
from nltk import ngrams
from nltk.stem import *
import json
from pprint import pprint
import operator

stemmer = PorterStemmer()


with open('data.json') as f:
    data = json.load(f)

# pprint(data)

def _handle_text(d):
    text = d['text']
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


countsByGram = {}
for d in data:
    # print(d['text'])
    _handle_text(d)

sorted_x = sorted(countsByGram.items(), key=operator.itemgetter(1))

print(sorted_x)

# sentence = "i'm a vampire who loves to suck blood through platic straws so i am opposed to the straw ban"

# tokens = nltk.word_tokenize(sentence)
# print(tokens)
# tagged = nltk.pos_tag(tokens)
# print(tagged)
# entities = nltk.chunk.ne_chunk(tagged)
# print(entities)
# entities.draw()

# sixgrams = ngrams(sentence.split(), 6)
# for grams in sixgrams:
#   print(grams)
