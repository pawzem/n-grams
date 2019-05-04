import sys
import nltk
from collections import Counter


def main():
    print("performing analysis of digrams, trigrams and special chars\n")
    file_name = sys.argv[1]
    file = open(file_name, "rt")

    lines = file.readlines()
    ngrams_analysis(lines)

    file.close()


def ngrams_analysis(lines):
    text = ''
    for line in lines:
        text += line
    tokens = nltk.word_tokenize(text)
    trigrams = nltk.trigrams(tokens)
    bigrams = nltk.bigrams(tokens)
    print("digrams\n")
    analize(bigrams)
    print("trigrams\n")
    analize(trigrams)
    print("character count\n")
    analize_characters(text)


def analize_characters(text):
    counts = Counter(text)
    for character, count in counts.items():
        print("'{}' {}".format(character, count))


def analize(ngrams):
    dist = nltk.FreqDist(ngrams)
    for ngram, count in dist.items():
        print(ngram, count)


if __name__ == "__main__":
    main()
