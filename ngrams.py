import sys
import nltk


def main():
    print("performing analysis of digrams, trigrams and special chars\n")
    file_name = sys.argv[1]
    file = open(file_name, "rt")

    lines = file.readlines()
    trigrams(lines)

    file.close()


def trigrams(lines):
    tokens = []
    for line in lines:
        tokens.append(nltk.word_tokenize(line))
    print(list(nltk.trigrams(tokens)))
#     bigrams also avilible


if __name__ == "__main__":
    main()
