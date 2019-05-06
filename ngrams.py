import sys
import nltk
import json
from collections import Counter


def main():
    print("performing analysis of digrams, trigrams and special chars\n")
    file_name = sys.argv[2]
    file = open(file_name, "rt", encoding="utf8")

    lines = file.readlines()
    analysis = ngrams_analysis(lines)
    analysis['language'] = sys.argv[1]

    output_file = open(sys.argv[3], 'wt', encoding="utf8")
    json_dumps = json.dumps(analysis)
    output_file.write(json_dumps)

    file.close()


def ngrams_analysis(lines):
    text = ''
    for line in lines:
        text += line
    tokens = nltk.word_tokenize(text)

    trigrams = nltk.trigrams(tokens)
    bigrams = nltk.bigrams(tokens)

    digrams = analize(bigrams, len(text))
    trigrams = analize(trigrams, len(text))
    characters = analize_characters(text)

    return {'digrams': digrams, 'trigrams': trigrams, 'characters': characters}


def analize_characters(text):
    result = {}
    counts = Counter(text)
    for character, count in counts.items():
        result[character] = count / len(text)
    return result


def analize(ngrams, length):
    result = {}
    dist = nltk.FreqDist(ngrams)
    for ngram, count in dist.items():
        result["{}".format(ngram)] = count / length
    return result


if __name__ == "__main__":
    main()
