#!/usr/bin/env python3
import sys
import pprint

NGRAM_COUNT = 3
ngram_counts = {}


def ngrams(word, n):
    pad = [None for _ in range(n - 1)]
    x = pad + list(word) + pad
    return [tuple(chars) for chars in zip(*(x[i:] for i in range(n)))]


def read_lines_as_ngrams(from_file, n):
    with open(from_file, 'r') as f:
        for line in f:
            word = line.strip()
            yield word, ngrams(word, n)


for word, ngram_list in read_lines_as_ngrams(sys.argv[1], NGRAM_COUNT):
    for ngram in ngram_list:
        if ngram not in ngram_counts:
            ngram_counts[ngram] = 0
        ngram_counts[ngram] += 1


pprint.pprint(ngram_counts)
